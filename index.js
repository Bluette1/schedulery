const celery = require('celery-node');

async function runTask() {
  // Connect to the Redis broker
  const client = celery.createClient(
    'redis://localhost:6379/0', // broker URL
    'redis://localhost:6379/0'  // backend URL
  );

  try {
    // Define the reminder task you want to call
    const reminderTask = client.createTask('tasks.send_reminder');

    // Manually trigger the reminder task
    const message = 'This is your manual reminder!';

    const task = reminderTask.applyAsync([message]);

    // Wait for the result
    const result = await task.get();
    console.log('Result:', result);
  } catch (err) {
    console.error('Error:', err);
  } finally {
    // Close the client connection when done
    client.disconnect();
  }
}

runTask();