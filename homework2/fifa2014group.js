

var request = require("request");
request("http://worldcup.kimonolabs.com/api/teams?apikey=IzEDFq3HeYdzTAtHV060PIBA5CeIte3E&group="+process.argv[2],
function(err, response, body) {
        var jsonObject = JSON.parse(body);
        console.log("Name             W  D  L");
        jsonObject.sort(function(a,b){
        return a["groupRank"]>b["groupRank"];
});
for(var i in jsonObject){
        while(jsonObject[i]['name'].length<17)
                jsonObject[i]['name']=jsonObject[i]['name']+" ";
        console.log(jsonObject[i]['name']+jsonObject[i]["wins"]+"  "+jsonObject[i]["draws"]+"  "+jsonObject[i]["losses"]);
        }
});
