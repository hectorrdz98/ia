
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
    drawTexts();
    drawHiddenLayers();
}

function drawTexts() {
    push();
    noStroke();
    fill(255);
    strokeWeight(3);
    textSize(20);
    textAlign(CENTER, CENTER);
    text("x: " + testData[0], 100, 50);
    text("y: " + testData[1], 100, 75);
    stroke(255);
    line(80, 100, 120, 100);
    noStroke();
    if ( testData[2] ) {
        text("( " + testData[2] + ", " + testData[3] + " )", 100, 125);
    }
    pop();
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
        if (hiddenL.win)
            fill(60, 87, 161);
        circle(300, 100 + (i * 150), 100);
        if (hiddenL.win)
            fill(255);
        else
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
                result: null,
                win: false
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
        var max = null;
        for (let i = 0; i < hiddenLayers.length; i++) {
            const hiddenL = hiddenLayers[i];
            hiddenL.win = false;
            hiddenL.result = 
                ((testData[2] * hiddenL.nW[0]) + 
                (testData[3] * hiddenL.nW[1])).toFixed(2);
            if (max) {
                if (max.result < hiddenL.result)
                    max = hiddenL;
            } else {
                max = hiddenL;
            }
        }
        if (max) {
            max.win = true;
        }
    }
});

function findInHidden(name) {
    for (let i = 0; i < hiddenLayers.length; i++) {
        if (hiddenLayers[i].name == name) return hiddenLayers[i];
    }
    return null;
}