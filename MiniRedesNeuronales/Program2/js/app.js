
var examples = [];
var testData = [0, 0];

$("#hiddenBtn").click(function () {
    var name = $("#inputName").val();
    var x = parseFloat($("#inputX").val());
    var y = parseFloat($("#inputY").val());

    if (name != "" && x != "" && y != "") {
        examples.push({
            name: name,
            w: [x, y],
            distance: 0
        });

        var output = `
            <tr>
                <th>` + name + `</th>
                <td>` + x + `</td>
                <td>` + y + `</td>
                <td>0</td>
            </tr>
        `;
        $("#examplesTable").append(output);
    }
});

$("#testBtn").click(function () {
    var x = parseFloat($("#inputTestX").val());
    var y = parseFloat($("#inputTestY").val());
    var k = parseFloat($("#inputTestK").val());

    if (x != "" && y != "" && k != "") {
        for (let i = 0; i < examples.length; i++) {
            const example = examples[i];
            example.distance = Math.sqrt( ((example.w[0] - x) ** 2) + ((example.w[1] - y) ** 2) );
        }

        examples.sort(function(a, b){
            if(a.distance < b.distance) return -1;
            if(a.distance > b.distance) return 1;
            return 0;
        });
        
        updateTable(k);
        var kExamples = examples.slice(0, k);
        var result = findMostFreq(kExamples);

        if (result)
            $("#resultsLabel").html("The result of [" + x + ", " + y + "] is <b>" + result.name + "!</b>");
        else
            $("#resultsLabel").html("Not enough examples to predict");
    }
});

function updateTable(k) {
    $("#examplesTable").empty();
    for (let i = 0; i < examples.length; i++) {
        const example = examples[i];
        
        if (i < k) {
            var output = `
                <tr style="background-color: #5E93DB; color: white;">
            `;
        } else {
            var output = `
                <tr>
            `;
        }

        output += `
                <td>` + example.name + `</td>
                <td>` + example.w[0] + `</td>
                <td>` + example.w[1] + `</td>
                <td>` + example.distance + `</td>
            </tr>
        `;

        $("#examplesTable").append(output);
    }
}

function findMostFreq(kExamples) {
    var appears = [];
    for (let i = 0; i < kExamples.length; i++) {
        const example = kExamples[i];
        var found = findInArray(appears, example.name);
        if (found) {
            found.total++;
        } else {
            appears.push({
                name: example.name,
                total: 1
            });
        }
    }
    appears.sort(function(a, b){
        if(a.total > b.total) return -1;
        if(a.total < b.total) return 1;
        return 0;
    });
    return appears != [] ? appears[0] : null;
}

function findInArray(array, nameToFind) {
    for (let i = 0; i < array.length; i++) {
        if (array[i].name == nameToFind) return array[i];
    }
    return null;
}