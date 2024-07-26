const neo4j = require('neo4j-driver');

// Replace with your Neo4j instance details
const URI = 'bolt://localhost:7687';
const USER = 'neo4j';
const PASSWORD = '12345678';

const driver = neo4j.driver(URI, neo4j.auth.basic(USER, PASSWORD));

async function connectAndRetrieve() {
  const session = driver.session();
  try {
    const result = await session.run('MATCH (n) RETURN n LIMIT 1');
    console.log(result.records);
  } catch (error) {
    console.error('Error connecting to Neo4j', error);
  } finally {
    await session.close();
  }
}

connectAndRetrieve().then(() => driver.close());