
var menuActive = false;
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

$("#btn-perm").click(function () {
    var id = $("#node-id").val();
    if (id != "") {
        var initNode = getNodeById(id);
        initialNode = initNode;
        if (initNode) {
            initNode.visited = true;
            paths = [];
            lowestPath = null;
            runSimulation(initNode, [0], [initNode]);
            appendPaths();
            initNode.visited = false;
        }
    }
});

var path2Draw = null;

$(document).on('click', '.path-selector', function(){ 
    var pathID = parseInt($(this).attr("id").substring(5));
    path2Draw = paths[pathID];
}); 

var initialNode = null;

var maxTamCanvas = [1280, 720];

function setup() {
    var myCanvas = createCanvas(windowWidth, windowHeight);
    myCanvas.parent("design-container");
}

class Node {
    constructor(x, y) {
        this.id = getNodeId().toString();
        this.x = x;
        this.y = y;
        this.visited = false;
        this.nextNode = null;
        this.d = parseInt(random(50, 75));
        this.color = [parseInt(random(0, 255)), parseInt(random(0, 255)), parseInt(random(0, 255))];
    }
}

var nodes = [];
var paths = [];
var lowestPath = null;

function getNodeById(id) {
    for (let i = 0; i < nodes.length; i++) {
        if (nodes[i].id == id) return nodes[i];
    }
    return null;
}

function getNodeId() {
    var a = 1;
    var cont = true;
    var ids = [];

    for (let i = 0; i < nodes.length; i++) {
        ids.push(nodes[i].id);
    }

    while (cont) {
        var found = ids.indexOf(a.toString());
        if (found == -1) break;
        a++;
    }
    
    return a;
}

function runSimulation(initNode, lengths, path) {
    for (let i = 0; i < nodes.length; i++) {
        if (!nodes[i].visited) {
            // console.log(initNode.id + " -> " + nodes[i].id);

            var nodesWidth = abs(initNode.x - nodes[i].x);
            var nodesHeight = abs(initNode.y - nodes[i].y);

            var dist = sqrt(pow(nodesWidth, 2) + pow(nodesHeight, 2));
            // console.log("dist: " + dist);
            lengths.push(dist);
            path.push(nodes[i]);
            // console.log(path);

            nodes[i].visited = true;
            initNode.nextNode = nodes[i];
            runSimulation(nodes[i], lengths, path);

            path.pop();
            lengths.pop();
            nodes[i].visited = false;
            initNode.nextNode = null;
        }
    }

    if (lengths.length == nodes.length) {
        var nodesWidth = abs(initialNode.x - path[path.length-1].x);
        var nodesHeight = abs(initialNode.y - path[path.length-1].y);

        var dist = sqrt(pow(nodesWidth, 2) + pow(nodesHeight, 2));
        lengths.push(dist);
        path.push(initialNode);

        paths.push({
            'dist': lengths.reduce((a, b) => a + b),
            'path': path.slice(),
            'color': [parseInt(random(0, 255)), parseInt(random(0, 255)), parseInt(random(0, 255))]
        });

        if (!lowestPath || lengths.reduce((a, b) => a + b) < lowestPath.dist)
            lowestPath = paths[paths.length-1];

        path.pop();
        lengths.pop();
    }

}

function appendPaths() {
    $("#paths-div").empty();
    var otp = "";
    lowestPath.path.forEach(e => {
        otp += e.id + " ";
    });
    $("#lowestPath").text("Lowest Path: " + otp);
    $("#lowestDist").text("Lowest Distance: " + lowestPath.dist.toFixed(2));
    path2Draw = lowestPath;

    var cont = 0;
    paths.forEach(path => {
        var output = `
            <div style="margin-bottom: 1.5rem;">
                <h2 class="subtitle" style="display: flex; align-items: center; margin-bottom: 0px;">
                    <div id="path_` + cont + `" class="path-selector" style="width: 20px; height: 20px;
                        background-color: rgb(` + path.color[0] +  `, ` + 
                            path.color[1] + `, ` + path.color[2] + `);
                        margin-right: 20px;"></div>
        `;
        path.path.forEach(elem => {
            output += elem.id + ` `;
        });
        output += `
                </h2>
                <span style="font-size: 12px">Distance: ` + path.dist.toFixed(2) + `</span>
            </div>
        `;
        pathsDiv.append(output);
        cont++;
    });
}

function draw() {
    clear();
    background(70, 66, 74);
    drawNodes();
    drawPath(path2Draw);
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
    var nodeFound = findNode(mouseX, mouseY);
    if (nodeFound != null) {
        var index = nodes.indexOf(nodeFound);
        if (index > -1) {
            nodes.splice(index, 1);
        }
    }
    else {
        nodes.push(new Node(mouseX, mouseY));
    }
}

function drawNodes() {
    push();
    nodes.forEach(node => {
        if (node == initialNode) {
            stroke(255);
            strokeWeight(4);
            fill(0);
        }
        else {
            noStroke();
            fill(node.color[0], node.color[1], node.color[2]);
        }
        circle(node.x, node.y, node.d);
        fill(255);
        textSize(20);
        textAlign(CENTER, CENTER);
        text(node.id, node.x - (node.d / 2), node.y - (node.d / 2), node.d, node.d);
    });
    pop();
}

function drawPath(path) {
    if (path) {
        push();
        noFill();
        stroke(path.color[0], path.color[1], path.color[2]);
        strokeWeight(4);
        for (let j = 0; j < path.path.length-1; j++) {
            const elem = path.path[j];
            line(elem.x, elem.y, path.path[j+1].x, path.path[j+1].y);
            /*push();
            var angle = atan2(elem.y - path.path[j+1].y, elem.x - path.path[j+1].x);
            translate(path.path[j+1].x, path.path[j+1].y);
            rotate(angle-HALF_PI);
            stroke(path.color[0], path.color[1], path.color[2]);
            fill(255);
            triangle(10, 10, -10, 10, 0, -10);
            pop();*/
        }
        pop();
    }
}

function findNode(x, y) {
    for (let i = 0; i < nodes.length; i++) {
        const node = nodes[i];
        if (x >= (node.x - (node.d / 2)) && x <= (node.x + (node.d / 2)) &&
            y >= (node.y - (node.d / 2)) && y <= (node.y + (node.d / 2))) return node;
    }
    return null;
}