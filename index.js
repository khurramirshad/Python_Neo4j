

function submitQuery() {
    const neo4j = require('neo4j-driver');


    const driver = neo4j.driver('bolt://localhost:7687', neo4j.auth.basic('neo4j', '12345678'));
    //auth=("neo4j", "12345678"
    const session = driver.session();


    alert("Submit query");
    const query = document.getElementById('query').value;
    alert(query);
    session.run(query).then(result => {
        const nodes = [];
        const links = [];

        result.records.forEach(record => {
            record._fields.forEach(field => {
                if (field.start && field.end) {
                    links.push({ source: field.start.identity.low, target: field.end.identity.low });
                } else {
                    nodes.push({ id: field.identity.low, label: field.labels[0] });
                }
            });
        });

        drawGraph(nodes, links);
    });
}

function drawGraph(nodes, links) {
    alert("Draw graph");
    alert(nodes);
    const canvas = document.getElementById('graphCanvas');
    const context = canvas.getContext('2d');

    const simulation = d3.forceSimulation(nodes)
        .force('link', d3.forceLink(links).id(d => d.id))
        .force('charge', d3.forceManyBody())
        .force('center', d3.forceCenter(canvas.width / 2, canvas.height / 2));

    simulation.on('tick', () => {
        context.clearRect(0, 0, canvas.width, canvas.height);

        links.forEach(link => {
            context.beginPath();
            context.moveTo(link.source.x, link.source.y);
            context.lineTo(link.target.x, link.target.y);
            context.stroke();
        });

        nodes.forEach(node => {
            context.beginPath();
            context.arc(node.x, node.y, 5, 0, 2 * Math.PI);
            context.fill();
        });
    });
}