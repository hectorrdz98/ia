
var menuActive = true;
var pathsDiv = $("#paths-div");

$("#diagram-show-menu").click(function () {
    if ($("#diagram-menu").css("transform") == "matrix(1, 0, 0, 1, -350, 0)") {
        $("#diagram-menu").css("transform", "translateX(0px)");
        $("#diagram-show-menu i").css("transform", "rotate(180deg)");
        menuActive = true;
    } else {
        $("#diagram-menu").css("transform", "translateX(-350px)");
        $("#diagram-show-menu i").css("transform", "rotate(0deg)");
        setTimeout(function(){ menuActive = false; }, 500);
    }
});

var nodes = [];
var kNodes = [];
var iter = 0;

class Node {
    constructor(x, y) {
        this.x = x;
        this.y = y;
        this.color = null;
        this.parent = null;
        this.children = [];
    }
}

$("#btnRestart").click(function () {
    nodes = [];
    for (let i = 0; i < 10000; i++) {
        nodes.push( 
            new Node(
                Math.floor(Math.random() * maxTamCanvas[0]), 
                Math.floor(Math.random() * maxTamCanvas[1])
            ) 
        );
    }
});

$("#btnCluster").click(function () {
    fitNodes();
});

var maxTamCanvas = [1536, 754];

function setup() {
    var myCanvas = createCanvas(windowWidth, windowHeight);
    myCanvas.parent("design-container");
}

function draw() {
    clear();
    background(70, 66, 74);
    drawNodes();
    drawKNodes();
}

function mouseClicked() {
    if (menuActive) {
        if (mouseX > 400 && (mouseX < 1130 || mouseY < 550)) {
            clickEvent();
        }
    } else {
        if (mouseX > 50 && (mouseX < 1130 || mouseY < 550)) {
            clickEvent();
        }
    }
}

function clickEvent() {
    var node = new Node(mouseX, mouseY);
    node.color = [
        Math.floor(Math.random() * 255),
        Math.floor(Math.random() * 255),
        Math.floor(Math.random() * 255)
    ];
    kNodes.push(node);
    $("#labelK").text("K: " + kNodes.length);
}

function drawNodes() {
    nodes.forEach(node => {
        push();
        noStroke();

        if (node.parent) {
            fill(node.parent.color);
        } else {
            fill(255);
        }
        
        circle(node.x, node.y, 5);
        pop();
    });
}

function drawKNodes() {
    kNodes.forEach(node => {
        push();
        stroke(255);
        fill(node.color);
        circle(node.x, node.y, 20);
        pop();
    });
}

function fitNodes() {
    var changes = 0;

    kNodes.forEach(knode => {
        knode.children = [];
    });
    nodes.forEach(node => {
        var best = null;
        var bestDist = 0;
        kNodes.forEach(knode => {
            if (best) {
                var dist = Math.sqrt( ((knode.x - node.x) ** 2) + ((knode.y - node.y) ** 2) );
                if (dist < bestDist) {
                    best = knode;
                    bestDist = dist;
                }
            } else {
                best = knode;
                bestDist = Math.sqrt( ((knode.x - node.x) ** 2) + ((knode.y - node.y) ** 2) );
            }
        });
        if (best) {
            if (node.parent != best) {
                changes++;
            }
            node.parent = best;
            best.children.push(node);
        }
    });

    kNodes.forEach(knode => {
        var promX = 0;
        var promY = 0;
        knode.children.forEach(node => {
            promX += node.x;
            promY += node.y;
        });
        if (knode.children.length > 0) {
            knode.x = promX / knode.children.length;
            knode.y = promY / knode.children.length;
        }
    });

    if (changes > 0) {
        fitNodes();
        iter++;
        $("#labelIte").text("Iterations: " + iter);
    }
}