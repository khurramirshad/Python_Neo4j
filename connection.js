define('neo4jModule2', ['neo4j-driver'], function(neo4j) {
  // Replace with your Neo4j instance details
  const URI = 'bolt://localhost:7687';
  const USER = 'neo4j';
  const PASSWORD = '12345678';
  
  const driver = neo4j.driver(URI, neo4j.auth.basic(USER, PASSWORD));

  async function connect() {
    const session = driver.session();
    console.log("Hello");
    try {
      const result = await session.run('MATCH (n) RETURN n LIMIT 1');
      console.log(result.records);
    } catch (error) {
      console.error('Error connecting to Neo4j', error);
    } finally {
      await session.close();
    }
  }

  connect().then(() => driver.close());
});

  function submitQuery() {}