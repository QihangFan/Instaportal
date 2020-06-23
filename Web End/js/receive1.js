var adafruitUsername = 'fqhang';
var adafruitFeed1 = 'knobvalue1';
var knob1V = 0;
var adafruitFeed2 = 'knobvalue2';
var knob2V = 0;
var adafruitFeed3 = 'photosensor';
var lightV = 0;
var adafruitFeed4 = 'temperature';
var tempV = 0;
var adafruitFeed5 = 'humidity';
var humidV = 0;
var adafruitAioKey = 'f8c8109354ca4d83b7a702d9101b2fc4';



setInterval(function(){
  getAdaIO(adafruitUsername, adafruitFeed1, adafruitAioKey, knob1);
  getAdaIO(adafruitUsername, adafruitFeed2, adafruitAioKey, knob2);
  getAdaIO(adafruitUsername, adafruitFeed3, adafruitAioKey, light);
  getAdaIO(adafruitUsername, adafruitFeed4, adafruitAioKey, temp);
  getAdaIO(adafruitUsername, adafruitFeed5, adafruitAioKey, humid);
  changeimg();
}, 2000);



//people 9 animal 2 fengjing 6
function knob1(data) {
    var knob1Num = parseInt(data);
    knob1V = knob1Num;
}
function knob2(data) {
    var knob2Num = parseInt(data);
    knob2V = knob2Num;
}
function light(data) {
    var lightNum = parseInt(data);
    if (lightNum < 2) {
      lightV = 1; //night
    } else if (lightNum < 7) {
      lightV = 2; //average
    } else {
      lightV = 2; //bright sunshine
    }
}
function temp(data) {
    var tempNum = parseInt(data);
    if (tempNum < 1) {
      tempV = 1; //0C
    } else if (tempNum < 50) {
      tempV = 2; //<10C
    } else if (tempNum < 68) {
      tempV = 3; //<20C
    } else if (tempNum < 77) {
      tempV = 4; //<25C
    } else if (tempNum < 86) {
      tempV = 5; //<30C
    } else {
      tempV = 6; //>30C
    }
}

function temp(data) {
    var tempNum = parseInt(data);
    if (tempNum < 1) {
      tempV = 1; //0C
    } else if (tempNum < 50) {
      tempV = 2; //<10C
    } else if (tempNum < 68) {
      tempV = 3; //<20C
    } else if (tempNum < 77) {
      tempV = 4; //<25C
    } else if (tempNum < 86) {
      tempV = 5; //<30C
    } else {
      tempV = 6; //>30C
    }
}
function humid(data) {
    var humidNum = parseInt(data);
    if (humidNum < 40) {
      humidV = 1; // dry
    } else if (humidNum < 70) {
      humidV = 2; // average
    } else {
      humidV = 3; // humid
    }
}


function changeimg() {
  var getdata = knob1V.toString() + knob2V.toString() + lightV.toString() + tempV.toString() + humidV.toString();
  //var getdata = knob1V.toString() + knob2V.toString() + lightV.toString();
  console.log(getdata);

  if (getdata == "61242") {
    $("#img61242").show();
    $("#img66142").hide();
    $("#img66242").hide();
    $("#img66342").hide();
    $("#img69242").hide();
    $("#img91242").hide();
    $("#img92142").hide();
    $("#img96142").hide();
    $("#img96242").hide();
    $("#img96342").hide();
    $("#img99242").hide();
  } else if (getdata == "66142") {
    $("#img66142").show();
    $("#img61242").hide();
    $("#img66242").hide();
    $("#img66342").hide();
    $("#img69242").hide();
    $("#img91242").hide();
    $("#img92142").hide();
    $("#img96142").hide();
    $("#img96242").hide();
    $("#img96342").hide();
    $("#img99242").hide();
  } else if (getdata == "66242"){
    $("#img66242").show();
    $("#img61242").hide();
    $("#img66142").hide();
    $("#img66342").hide();
    $("#img69242").hide();
    $("#img91242").hide();
    $("#img92142").hide();
    $("#img96142").hide();
    $("#img96242").hide();
    $("#img96342").hide();
    $("#img99242").hide();
  } else if (getdata == "66342"){
    $("#img66342").show();
    $("#img61242").hide();
    $("#img66142").hide();
    $("#img66242").hide();
    $("#img69242").hide();
    $("#img91242").hide();
    $("#img92142").hide();
    $("#img96142").hide();
    $("#img96242").hide();
    $("#img96342").hide();
    $("#img99242").hide();
  } else if (getdata == "69242"){
    $("#img69242").show();
    $("#img61242").hide();
    $("#img66142").hide();
    $("#img66242").hide();
    $("#img66342").hide();
    $("#img91242").hide();
    $("#img92142").hide();
    $("#img96142").hide();
    $("#img96242").hide();
    $("#img96342").hide();
    $("#img99242").hide();
  } else if (getdata == "91242"){
    $("#img91242").show();
    $("#img61242").hide();
    $("#img66142").hide();
    $("#img66242").hide();
    $("#img66342").hide();
    $("#img69242").hide();
    $("#img92142").hide();
    $("#img96142").hide();
    $("#img96242").hide();
    $("#img96342").hide();
    $("#img99242").hide();
  } else if (getdata == "92142"){
    $("#img92142").show();
    $("#img61242").hide();
    $("#img66142").hide();
    $("#img66242").hide();
    $("#img66342").hide();
    $("#img69242").hide();
    $("#img91242").hide();
    $("#img96142").hide();
    $("#img96242").hide();
    $("#img96342").hide();
    $("#img99242").hide();
  } else if (getdata == "96142"){
    $("#img96142").show();
    $("#img61242").hide();
    $("#img66142").hide();
    $("#img66242").hide();
    $("#img66342").hide();
    $("#img69242").hide();
    $("#img91242").hide();
    $("#img92142").hide();
    $("#img96242").hide();
    $("#img96342").hide();
    $("#img99242").hide();
  } else if (getdata == "96242"){
    $("#img96242").show();
    $("#img61242").hide();
    $("#img66142").hide();
    $("#img66242").hide();
    $("#img66342").hide();
    $("#img69242").hide();
    $("#img91242").hide();
    $("#img92142").hide();
    $("#img96142").hide();
    $("#img96342").hide();
    $("#img99242").hide();
  } else if (getdata == "96342"){
    $("#img96342").show();
    $("#img61242").hide();
    $("#img66142").hide();
    $("#img66242").hide();
    $("#img66342").hide();
    $("#img69242").hide();
    $("#img91242").hide();
    $("#img92142").hide();
    $("#img96142").hide();
    $("#img96242").hide();
    $("#img99242").hide();
  } else if (getdata == "99242"){
    $("#img99242").show();
    $("#img61242").hide();
    $("#img66142").hide();
    $("#img66242").hide();
    $("#img66342").hide();
    $("#img69242").hide();
    $("#img91242").hide();
    $("#img92142").hide();
    $("#img96142").hide();
    $("#img96242").hide();
    $("#img96342").hide();
  } else {
    $("#img61242").hide();
    $("#img66142").hide();
    $("#img66242").hide();
    $("#img66342").hide();
    $("#img69242").hide();
    $("#img91242").hide();
    $("#img92142").hide();
    $("#img96142").hide();
    $("#img96242").hide();
    $("#img96342").hide();
    $("#img99242").hide();
    $("#canvas").text("Oops, no pic matches your situation.");
  }
}
