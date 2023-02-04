$( document ).ready(function() {
    console.log( "ready!" );
});
$("#id_btn_calc").click(function()
/*{
  console.log("Test");
  prevDate = $("#id_prevdateinmillisec").val();
  nextDate = $("#id_nextdateinmillisec").val();
  prevReading = $("#id_prevreading").val();
  nextReading = $("#id_nextreading").val();
  periodInDays = (1.0 * (nextDate - prevDate)/(24*60*60*1000));
  readingDiff = nextReading - prevReading;
  isSave=$("#id_isSave").val();
  console.log(periodInDays)
  $("#div_units").text(readingDiff)
  $("#div_days").text(periodInDays)
}
); 
void onCalculateClicked() 
*/
{
    // {
    var priceModels=[];
    PriceModel.init(priceModels);
    
    var prevReading = $("#id_prevreading").val();
    var nextReading = $("#id_nextreading").val();
    var prevDate = $("#id_prevdateinmillisec").val();
    //console.log(prevDate);
    prevDate = new Date(prevDate).getTime();
    //console.log(prevDate);
    var nextDate = $("#id_nextdateinmillisec").val();
    //console.log(nextDate);
    nextDate = new Date(nextDate).getTime();
    //console.log(nextDate);
    PriceModel.setPriceModelsPeriods(priceModels, prevDate, nextDate, prevReading, nextReading);

    //show the whole period and units:
    var periodInDays = Math.round (1.0 * (nextDate - prevDate)/(24*60*60*1000));
    var readingDiff = nextReading - prevReading;
    $("#div_units").text(readingDiff)
    $("#div_days").text(periodInDays)
    //textViewUnits.setText(String.format("%d",readingDiff));
    //textViewPeriod.setText(String.format("%d", (int) periodInDays));
    //}
    var price = 0;
    var calcString = "";
    for(var i=0; i<priceModels.length; i++) {
        var pm = priceModels[i];
        if(pm.applied) {
            pm.getPrice();
            price += pm.price;//getPrice(nextDate, prevDate);
            if(!calcString===""){
                calcString +="+";
            }
            calcString += "("+pm.calculationString+")";
            //double periodInDays= 1.0 * (pm.nDate - pm.pDate)/(24*60*60*1000);
            //readingDiff = pm.nextReading - pm.prevReading;
        }
    }

    //priceTextView.setText(String.format("%.0f",price));
    //calcTextView.setText(calcString);
    $("#div_price").text(Math.round(price))
    $("#div_calc").text(calcString)
    
    //storeSettings();
    var isSave=$("#id_isSave").is(':checked');
    //console.log("--------------")
    //console.log(isSave)
    if(isSave) {
        //saveValues(price, calcString);
        //submit
        //console.log("--------------")
        //console.log(calcString)
        $("#id_price").val(Math.round(price))
        $("#id_calcstr").val(calcString)
        
        /*$("<input />").attr("type", "hidden")
          .attr("name", "calcstr")
          .attr("value", calcString)
          .appendTo("#my_form");
        $("<input />").attr("type", "hidden")
          .attr("name", "price")
          .attr("value", Math.round(price))
          .appendTo("#my_form");*/
        
        //$('#my_form').submit();
        $(this).closest('form').submit();
    }
}    
); 


class PriceModel {
    /*var  description;
    var  applied; //used to indicate whether to include it in calc.
    var  appliedDate;
    var  pDate, nDate;  //prev & next dates
    var  prevReading, nextReading;
    var  unitPerMonth = [];
    var pricePerUnit=[];

    var calculationString;
    var price;*/

    constructor(desc, date, units, prices) {
        
        var arraySize = units.length;
        if(units.length != prices.length) {
            //should print error
        }
        this.description = desc;
        this.appliedDate = date;
        //this.unitPerMonth = new ArrayList<Integer>();
        //this.pricePerUnit = new ArrayList<Integer>();
        this.unitPerMonth=[];
        this.pricePerUnit =[];
        for (var i =0; i<arraySize; i++) {
            this.unitPerMonth[i] = units[i];
            this.pricePerUnit[i] = prices[i];
        }
    }
        
    //nDate&pDate are in milliSec
    getPrice() {
        var periodInDays= 1.0 * (this.nDate - this.pDate)/(24*60*60*1000);
        var readingDiff = this.nextReading - this.prevReading;
        //unitsPerPeriod;

        
        this.price = 0.0;
        this.calculationString = "";
        for (var i=0; i<this.unitPerMonth.length && readingDiff > 0; i++) {
            if(i>0) {
                this.calculationString += " + ";
            }
            var totalUnits = getUnitsPerPeriod(this.unitPerMonth[i], periodInDays);//unitsPerPeriod;
            
            if (readingDiff >= totalUnits) {
                this.price += totalUnits * this.pricePerUnit[i];
                readingDiff -= totalUnits;
                this.calculationString += totalUnits + "x" + this.pricePerUnit[i];
            } else {
                this.price += readingDiff * this.pricePerUnit[i];
                this.calculationString += readingDiff + "x" + this.pricePerUnit[i];
                break;
            }
        }
    }
        
    static init(priceModels) {
        //fill price model
        //Calendar c = Calendar.getInstance(TimeZone.getTimeZone("GMT"));
        //instantiate old Model
        //PriceModel pm1;
        var units4Months1 = [1000, 1000, 1000, Number.MAX_SAFE_INTEGER];//last units range is limitless
        var price4units1 =  [10,   20,   40,   80];
        var pm1 = new PriceModel("Old Model", 0, units4Months1, price4units1);
        priceModels.push(pm1);

        //Model started on 2016
        //c.set(2016, Calendar.JANUARY,1, 0, 0, 0);
        //c.set(Calendar.MILLISECOND, 0);
        var aDate = new Date('2016-01-01').getTime();//c.getTimeInMillis();
        var units4Months = [1000, 500, 500, 1000, 1000, Number.MAX_SAFE_INTEGER];//last units range is limitless
        var price4units =  [10,   20,  40,  80,   120, 200];
        pm1 = new PriceModel("Initial Model", aDate, units4Months, price4units);
        priceModels.push(pm1);

        //Model started on 2018
        //c.set(2018, Calendar.FEBRUARY,1, 0, 0, 0);
        //c.set(Calendar.MILLISECOND, 0);
        aDate = new Date('2018-02-01').getTime();//c.getTimeInMillis();
        var units4Months2 = [1500, 1500, 1000, Number.MAX_SAFE_INTEGER];//last units range is limitless
        var price4units2 =  [10,   35,   80,    120];
        pm1 = new PriceModel("2018 Model", aDate, units4Months2, price4units2);
        priceModels.push(pm1);
        
        //loadSettings();
    }
    
    static setPriceModelsPeriods(priceModels, prevDate, nextDate, prevReading, nextReading){
        //int k;
        //PriceModel pm1;
        for(var k =0; k<priceModels.length-1; k++) {
            var pm1 = priceModels[k];
            var pm2 = priceModels[k+1];
            //prevDate must be < nextDate
            if(prevDate >= pm1.appliedDate){
                if(prevDate <pm2.appliedDate) {
                    pm1.pDate = prevDate;
                    if (nextDate < pm2.appliedDate) {
                        pm1.nDate = nextDate;
                    } else {
                        pm1.nDate = pm2.appliedDate /*- 1000 * 3600 * 24*/;
                    }
                    pm1.applied = true;
                } else {
                    pm1.applied = false;
                }
            } else {
                if (nextDate >= pm1.appliedDate) {
                    pm1.pDate = pm1.appliedDate;
                    if(nextDate < pm2.appliedDate) {
                        pm1.nDate = nextDate;
                    } else {
                        pm1.nDate = pm2.appliedDate /*- 1000 * 3600 * 24*/;
                    }
                    pm1.applied = true;
                } else {
                    pm1.applied = false;
                }
            }
        }
        pm1 = priceModels[k];
        if(prevDate >= pm1.appliedDate){
            //if(prevDate <pm2.appliedDate)
            {
                pm1.pDate = prevDate;
                pm1.nDate = nextDate;
                pm1.applied = true;
            }
        } else {
            if (nextDate >= pm1.appliedDate) {
                pm1.pDate = pm1.appliedDate;
                pm1.nDate = nextDate;
                pm1.applied = true;
            } else {
                pm1.applied = false;
            }
        }
        //distribute readings between applied models
        var reading =0;
        for(var k =0; k<priceModels.length; k++) {
            var pm = priceModels[k];
            if(!pm.applied) {
                continue;
            }
            var totalPeriod = nextReading - prevReading;
            var delta = 1.0 * totalPeriod * (pm.nDate - pm.pDate+1000*3600*24)/(nextDate - prevDate+1000*3600*24);
            pm.prevReading =  reading;
            pm.nextReading = Math.round(1.0 * reading + delta);
            reading = pm.nextReading + 1;
            if(pm.nextReading < pm.prevReading) {
                //pm.nextReading = pm.prevReading;
            }
        }
    }
}

function getUnitsPerPeriod(unitsInMonth, periodInDays) {
    return Math.round(1.0 * unitsInMonth * periodInDays / 30.0);
}


