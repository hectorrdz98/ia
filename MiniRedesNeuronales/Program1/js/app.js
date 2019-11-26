
var canvasDiv = null;

function setup() {
    canvasDiv = document.getElementById("canvasContainer");
    var width = canvasDiv.offsetWidth;
    var height = canvasDiv.offsetHeight;
    var canvas = createCanvas(width, height);
    canvas.parent("canvasContainer");
}

function windowResized() {
    var width = canvasDiv.offsetWidth;
    var height = canvasDiv.offsetHeight;
    resizeCanvas(width, height);
}

var hiddenLayers = [];
var testData = [0, 0];

function draw() {
    clear();
    background(70, 66, 74);
    drawHiddenLayers();
}

function drawHiddenLayers() {
    push();
    for (let i = 0; i < hiddenLayers.length; i++) {
        const hiddenL = hiddenLayers[i];
        noStroke();
        fill(255);
        textSize(16);
        textAlign(CENTER, CENTER);
        text(hiddenL.name, 300, 100 + (i * 150) - 50 - 10);
        circle(300, 100 + (i * 150), 100);
        fill(55, 58, 54);
        text("w1: " + hiddenL.w[0], 300, 100 + (i * 150) - 10);
        text("w2: " + hiddenL.w[1], 300, 100 + (i * 150) + 10);
        fill(255);
        stroke(255);
        text("( " + hiddenL.nW[0] + ", " + hiddenL.nW[1] + " )", 300 + 75, 100 + (i * 150), 100);
        push();
        strokeWeight(3);
        line(300 + 200, 100 + (i * 150), 300 + 250, 100 + (i * 150));
        line(300 + 250, 100 + (i * 150), 300 + 250 - 10, 100 + (i * 150) + 10);
        line(300 + 250, 100 + (i * 150), 300 + 250 - 10, 100 + (i * 150) - 10);
        pop();
        stroke(171, 202, 233);
        text(hiddenL.result ? hiddenL.result : "", 300 + 250 + 50, 100 + (i * 150));
    }
    pop();
}

$("#hiddenBtn").click(function () {
    var name = $("#inputName").val();
    var x = parseFloat($("#inputX").val());
    var y = parseFloat($("#inputY").val());

    if (name != "" && x != "" && y != "") {
        var hiddenL = findInHidden(name);
        if (hiddenL) {
            hiddenL.w = [ x, y ];
        } else {
            hiddenLayers.push({
                name: name,
                w: [x, y],
                nW: [ (x / sqrt(pow(x, 2) + pow(y, 2))).toFixed(2),
                      (y / sqrt(pow(x, 2) + pow(y, 2))).toFixed(2) ],
                result: null
            });
        }
    }
});

$("#testBtn").click(function () {
    var x = parseFloat($("#inputTestX").val());
    var y = parseFloat($("#inputTestY").val());

    testData = [ x.toFixed(2), y.toFixed(2),
        (x / sqrt(pow(x, 2) + pow(y, 2))).toFixed(2), (y / sqrt(pow(x, 2) + pow(y, 2))).toFixed(2) ];

    if (x != "" && y != "") {
        for (let i = 0; i < hiddenLayers.length; i++) {
            const hiddenL = hiddenLayers[i];
            hiddenL.result = 
                ((testData[2] * hiddenL.nW[0]) + 
                (testData[3] * hiddenL.nW[1])).toFixed(2)
        }
    }
});

function findInHidden(name) {
    for (let i = 0; i < hiddenLayers.length; i++) {
        if (hiddenLayers[i].name == name) return hiddenLayers[i];
    }
    return null;
}