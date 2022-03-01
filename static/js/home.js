function calcul(){
    // try{
    var IGR = Number(document.getElementById('IGR').value);
    var KDR = Number(document.getElementById('KDR').value);
    var PDR = Number(document.getElementById('PDR').value);
    var FPR = Number(document.getElementById('FPR').value);
    var AFR = Number(document.getElementById('AFR').value);
    var CAR = Number(document.getElementById('CAR').value);
    var MWR = Number(document.getElementById('MWR').value);
    var PGR = Number(document.getElementById('PGR').value);
    var PBR = Number(document.getElementById('PBR').value);

    var IGS = Number(document.getElementById('IGS').value);
    var KDS = Number(document.getElementById('KDS').value);
    var PDS = Number(document.getElementById('PDS').value);
    var FPS = Number(document.getElementById('FPS').value);
    var AFS = Number(document.getElementById('AFS').value);
    var CAS = Number(document.getElementById('CAS').value);
    var MWS = Number(document.getElementById('MWS').value);
    var PGS = Number(document.getElementById('PGS').value);
    var PBS = Number(document.getElementById('PBS').value);

    var KDC = Number(document.getElementById('KDC').value);
    var PDC = Number(document.getElementById('PDC').value);
    var FPC = Number(document.getElementById('FPC').value);
    var AFC = Number(document.getElementById('AFC').value);
    var CAC = Number(document.getElementById('CAC').value);
    var MWC = Number(document.getElementById('MWC').value);

    var Ref = Number(document.getElementById('Ref').value);
    var SO = Number(document.getElementById('SO').value);
    var Cp = Number(document.getElementById('Cp').value);
    var pc = Number(document.getElementById('pc').value);

    var CTR = Number(document.getElementById('CTR').value);
    var STR = Number(document.getElementById('STR').value);

    var HSR = Number(document.getElementById('HSR').value);
    var HSD = Number(document.getElementById('HSD').value);
    var CRR = Number(document.getElementById('CRR').value);
    var CRD = Number(document.getElementById('CRD').value);
    var FCR = Number(document.getElementById('FCR').value);
    var FCD = Number(document.getElementById('FCD').value);
    var RDR = Number(document.getElementById('RDR').value);
    var RDD = Number(document.getElementById('RDD').value);

    var VWA = Number(document.getElementById('VWA').value);
    var VWpct = Number(document.getElementById('VWpct').value);
    var CKA = Number(document.getElementById('CKA').value);
    var CKpct = Number(document.getElementById('CKpct').value);
    var CLA = Number(document.getElementById('CLA').value);
    var CLpct = Number(document.getElementById('CLpct').value);

    //Ind'n Gaming
    var IGC = IGR * IGS;
    document.getElementById('IGC').value = IGC.toFixed(2);

    //Kidney Dialysis
    var KDC = KDR * KDS;
    document.getElementById('KDC').value = KDC.toFixed(2);

    //Pandemic
    var PDC = PDR * PDS;
    document.getElementById('PDC').value = PDC.toFixed(2);

    //Fair Pay
    var FPC = FPR * FPS;
    document.getElementById('FPC').value = FPC.toFixed(2);

    //Arts & Funding
    var AFC = AFR * AFS;
    document.getElementById('AFC').value = AFC.toFixed(2);

    //Clean Air
    var CAC = CAR * CAS;
    document.getElementById('CAC').value = CAC.toFixed(2);

    //Minimum Wage
    var MWC = MWR * MWS;
    document.getElementById('MWC').value = MWC.toFixed(2);

    //Minimum Wage
    var PGC = PGR * PGS;
    document.getElementById('PGC').value = PGC.toFixed(2);
        
    console.log("PGC"+PGC)
    //Minimum Wage
    var PBC = PBR * PBS;
    document.getElementById('PBC').value = PBC.toFixed(2);

    // Earnings Calculations
    var Earning = IGC + KDC + PDC + FPC + AFC + CAC + MWC + PGC + PBC + Ref + SO + Cp + pc
    
    //TAX Calculations
    document.getElementById('CTA').value = (CTR * Earning).toFixed(2)
    document.getElementById('STA').value = (STR * Earning).toFixed(2)

    var Taxtptal = ((CTR * Earning)+(STR * Earning)).toFixed(2)

    console.log("Taxtptal  "+Taxtptal)

    //rental and stay calculations

    var HS = HSR * HSD
    var CR = CRR * CRD
    var FC = FCR * FCD
    var RD = RDR * RDD
    var HSCRded = HS + CR + FC + RD

    console.log(HSCRded)

    document.getElementById('HSC').value = HS.toFixed(2)
    document.getElementById('CRC').value = CR.toFixed(2)
    document.getElementById('HSC').value = HS.toFixed(2)
    document.getElementById('CRC').value = CR.toFixed(2)

    var vwper = VWA * VWpct
    var vwbal = VWA - vwper
    document.getElementById('VWcre').value = vwper.toFixed(2)
    document.getElementById('VWba').value = vwbal.toFixed(2)

    var ckper = CKA * CKpct
    var ckbal = CKA - ckper
    document.getElementById('CKcre').value = ckper.toFixed(2)
    document.getElementById('CKba').value = ckbal.toFixed(2)

    var clper = CLA * CLpct
    var clbal = CLA - clper
    document.getElementById('CLcre').value = clper.toFixed(2)
    document.getElementById('CLba').value = clbal.toFixed(2)

    var credtot = vwper + ckper + clper

    netpay = Earning - (Taxtptal + HSCRded + credtot)

    document.getElementById("Grspy").innerHTML = '$ '+Earning.toFixed(2)
    document.getElementById("ntpy").innerHTML = '$ '+netpay.toFixed(2) 
    // }     
    // catch{
    //     alert("Check all the field you filled correct or not !..")
    // }

}