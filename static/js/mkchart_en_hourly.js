var chart_hourly = AmCharts.makeChart("pvs_chart_en_hourly", {
  "type": "serial",
  "addClassNames": true,
  "theme": "light",
    "legend": {
        "equalWidths": false,
        "useGraphSettings": true,
        "valueAlign": "left",
        "valueWidth": 120
    },
  "balloon": {
    "adjustBorderColor": false,
    "horizontalPadding": 10,
    "verticalPadding": 8,
    "color": "#ffffff"
  },
  "balloonDateFormat" : "JJ:NN",

  "dataProvider": pvs_data_en_hourly,
  /*
  "dataLoader": {
    "url": 'http://'+location.host+'/appeng/amchart/3/',
  },*/
  "valueAxes": [{
	  "id": "energyAxis",           
	  "axisAlpha": 0,
	  "gridAlpha":0,
	  "position": "left",
	  "title": "Hourly Energy(Wh)",
	  "stackType": "regular", 
     },
    /*{
     "id": "uvAxis",           
     "axisAlpha": 0,
     "gridAlpha":0,
     "position": "right",
     "title": "UV",
     
    },*/
    ],
  "startDuration": 1,
  "graphs": [{
		//"alphaField": "alpha",
		"balloonText": "<span style='font-size:12px;'>[[title]] in [[category]]<br><span style='font-size:20px;'>[[value]]</span> [[additional]]</span>",
        "fillAlphas": 0.6,
        "lineAlpha": 0.4,
		//"type": "column",
		"title": "PVI(1)",
		"valueField": "1",
		"valueAxis": "energyAxis",
		"dashLengthField": "dashLengthColumn",
        "type": "smoothedLine",
  	},
  	{
	    "alphaField": "alpha",
	    "balloonText": "<span style='font-size:12px;'>[[title]] in [[category]]<br><span style='font-size:20px;'>[[value]]</span> [[additional]]</span>",
        "fillAlphas": 0.6,
        "lineAlpha": 0.4,
	    //"type": "column",
	    "title": "PVI(2)",
	    "valueField": "2",
	    "valueAxis": "energyAxis",
	    "dashLengthField": "dashLengthColumn",
        "type": "smoothedLine",
	},
	/*{
    "id": "graph3",
    "balloonText": "<span style='font-size:12px;'>[[title]] in [[category]]<br><span style='font-size:20px;'>[[value]](max)</span> [[additional]]</span>",
    "bullet": "triangleUp",
    "lineThickness": 2,
    "bulletSize": 7,
    "bulletBorderAlpha": 1,
    "bulletColor": "#A9F5A9",
                //"fillColors" : "#A9F5A9",
    "useLineColorForBulletBorder": true,
    "bulletBorderThickness": 3,
    "fillAlphas": 0,
    "lineAlpha": 1,
    "title": "UV",
    "valueField": "uv",
    "valueAxis": "uvAxis",
	},*/
	],
    "chartCursor": {
        "cursorAlpha": 0,
        "zoomable": false,
        "categoryBalloonDateFormat": "JJ:NN",
    },
  "dataDateFormat": "YYYY-MM-DD JJ:NN:SS",
  "categoryField": "date",
  "categoryAxis": {
    "dateFormats": [{
      		"period":'hh', 
      		"format":'JJ:NN'
    	}, {
          	"period": 'JJ', 
          	"format": 'JJ:NN'
    	}, {
            "period": "DD",
            "format": "MMM DD"
        }, {
            "period": "WW",
            "format": "MMM DD"
        }, {
            "period": "MM",
            "format": "MMM"
        }, {
            "period": "YYYY",
            "format": "YYYY"
        }],
    "parseDates": true,
    "minPeriod" : "hh",
    "gridPosition": "start",
    "axisAlpha": 0,
    "tickLength": 0
  },
  "export": {
    "enabled": true
  },
  "panEventsEnabled": false,
});
