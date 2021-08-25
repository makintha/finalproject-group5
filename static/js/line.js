//  Well 7 forcasting vs actual.
var well_7_url = "/api/v1.0/Well7"

d3.json(well_7_url).then((data) => {

    console.log(data);

    // getting the data for plot
    var act = data.map(as => as.actual);
    var dat = data.map(as => as.date);
    var fore = data.map(as => as.forecast);
    // converting date format
    dat = dat.map((element) => {
        var d = new Date(element);
        return `${d.getMonth() + 1}/${d.getDate()}/${d.getFullYear()}`;
    });

    //  plot details

    var trace1 = {
        x: dat, y: act, name: "Actual Data", type: "scatter",
        mode: "lines",
    }
    var trace2 = {
        x: dat, y: fore, name: "Forecast Data", type: "scatter",
        mode: "lines",
    }

    var data = [trace1, trace2];
    //  layout details
    var layout = {
        title: `Well 7 Forecast Vs Actual`,
        xaxis: { title: "Date", tickangle: 45 },
        xaxis2: { title: "Date", tickangle: 45 },
        legend: { x: -0.2, y: 1, traceorder: 'normal' },
        autosize: true,
        width: 1500,
        height: 650,
        yaxis: { title: "GasRate", titlefont: { color: "red" }, tickfont: { color: "red" } },
        yaxis2: {
            title: 'GasRate',
            // titlefont: {color: 'rgb(148, 103, 189)'},
            // tickfont: {color: 'rgb(148, 103, 189)'},
            overlaying: 'y',
            side: 'right'
        }
    };

    const config = {
        displayModeBar: false,
    };
    //  plot

    Plotly.newPlot('plot7', data, layout, config);

    console.log(act);
    console.log(dat);
    console.log(fore);
});

// Well 8

var well_8_url = "/api/v1.0/Well8"

d3.json(well_8_url).then((data) => {

    console.log(data);
    var act = data.map(as => as.actual);
    var dat = data.map(as => as.date);
    var fore = data.map(as => as.forecast);

    dat = dat.map((element) => {
        var d = new Date(element);
        return `${d.getMonth() + 1}/${d.getDate()}/${d.getFullYear()}`;
    });

    var trace1 = { x: dat, y: act, name: "Actual Data" }
    var trace2 = { x: dat, y: fore, name: "Forecast Data" }

    var data = [trace1, trace2];

    var layout = {
        title: `Well 8 Forecast Vs Actual`,

        xaxis: { title: "Date", tickangle: 45 },
        xaxis2: { title: "Date ", tickangle: 45 },
        legend: { x: -0.2, y: 1, traceorder: 'normal' },
        autosize: true,
        width: 1500,
        height: 650,
        yaxis: { title: "GasRate", titlefont: { color: "red" }, tickfont: { color: "red" } },
        yaxis2: {
            title: 'GasRate',
            // titlefont: {color: 'rgb(148, 103, 189)'},
            // tickfont: {color: 'rgb(148, 103, 189)'},
            overlaying: 'y',
            side: 'right'
        }
    };
    const config = {
        displayModeBar: false,
    };

    Plotly.newPlot('plot8', data, layout, config);

    console.log(act);
    console.log(dat);
    console.log(fore);
});


//  Well 9


var well_9_url = "/api/v1.0/Well9"

d3.json(well_9_url).then((data) => {

    console.log(data);
    var act = data.map(as => as.actual);
    var dat = data.map(as => as.date);
    var fore = data.map(as => as.forecast);

    dat = dat.map((element) => {
        var d = new Date(element);
        return `${d.getMonth() + 1}/${d.getDate()}/${d.getFullYear()}`;
    });

    var trace1 = { x: dat, y: act, name: "Actual Data" }
    var trace2 = { x: dat, y: fore, name: "Forecast Data" }

    var data = [trace1, trace2];

    var layout = {
        title: `Well 9 Forecast Vs Actual`,

        xaxis: { title: "Date", tickangle: 45 },
        xaxis2: { title: "Date ", tickangle: 45 },
        legend: { x: -0.2, y: 1, traceorder: 'normal' },
        autosize: true,
        width: 1500,
        height: 650,
        yaxis: { title: "GasRate", titlefont: { color: "red" }, tickfont: { color: "red" } },
        yaxis2: {
            title: 'GasRate',
            // titlefont: {color: 'rgb(148, 103, 189)'},
            // tickfont: {color: 'rgb(148, 103, 189)'},
            overlaying: 'y',
            side: 'right'
        }
    };
    const config = {
        displayModeBar: false,
    };

    Plotly.newPlot('plot9', data, layout, config);

    console.log(act);
    console.log(dat);
    console.log(fore);
});


// Well 10

var well_10_url = "/api/v1.0/Well10"

d3.json(well_10_url).then((data) => {

    console.log(data);
    var act = data.map(as => as.actual);
    var dat = data.map(as => as.date);
    var fore = data.map(as => as.forecast);

    dat = dat.map((element) => {
        var d = new Date(element);
        return `${d.getMonth() + 1}/${d.getDate()}/${d.getFullYear()}`;
    });

    var trace1 = { x: dat, y: act, name: "Actual Data" }
    var trace2 = { x: dat, y: fore, name: "Forecast Data" }

    var data = [trace1, trace2];

    var layout = {
        title: `Well 10 Forecast Vs Actual`,

        xaxis: { title: "Date", tickangle: 45 },
        xaxis2: { title: "Date ", tickangle: 45 },
        legend: { x: -0.2, y: 1, traceorder: 'normal' },
        autosize: true,
        width: 1500,
        height: 650,
        yaxis: { title: "GasRate", titlefont: { color: "red" }, tickfont: { color: "red" } },
        yaxis2: {
            title: 'GasRate',
            // titlefont: {color: 'rgb(148, 103, 189)'},
            // tickfont: {color: 'rgb(148, 103, 189)'},
            overlaying: 'y',
            side: 'right'
        }
    };
    const config = {
        displayModeBar: false,
    };

    Plotly.newPlot('plot10', data, layout, config);

    console.log(act);
    console.log(dat);
    console.log(fore);
});

//  Well 15

var well_15_url = "/api/v1.0/Well15"

d3.json(well_15_url).then((data) => {

    console.log(data);
    var act = data.map(as => as.actual);
    var dat = data.map(as => as.date);
    var fore = data.map(as => as.forecast);

    dat = dat.map((element) => {
        var d = new Date(element);
        return `${d.getMonth() + 1}/${d.getDate()}/${d.getFullYear()}`;
    });

    var trace1 = { x: dat, y: act, name: "Actual Data" }
    var trace2 = { x: dat, y: fore, name: "Forecast Data" }

    var data = [trace1, trace2];

    var layout = {
        title: `Well 15 Forecast Vs Actual`,

        xaxis: { title: "Date", tickangle: 45 },
        xaxis2: { title: "Date ", tickangle: 45 },
        legend: { x: -0.2, y: 1, traceorder: 'normal' },
        autosize: true,
        width: 1500,
        height: 650,
        yaxis: { title: "GasRate", titlefont: { color: "red" }, tickfont: { color: "red" } },
        yaxis2: {
            title: 'GasRate',
            // titlefont: {color: 'rgb(148, 103, 189)'},
            // tickfont: {color: 'rgb(148, 103, 189)'},
            overlaying: 'y',
            side: 'right'
        }
    };
    const config = {
        displayModeBar: false,
    };

    Plotly.newPlot('plot15', data, layout, config);

    console.log(act);
    console.log(dat);
    console.log(fore);

});