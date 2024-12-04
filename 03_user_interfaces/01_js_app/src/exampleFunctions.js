


function blockingFunction() {

  console.log('Blocking function started');
  let i = 0;
  while (i < 10000000000) {
    i++;
  }
  console.log('Blocking function finished');
}

async function task1() {
  console.log('Task 1 started');
  return new Promise((resolve) =>
    setTimeout(() => {
      console.log('Task 1 finished');
      resolve('Result 1');
    }, 2000)
  );
}

async function task2() {
  console.log('Task 2 started');
  return new Promise((resolve) =>
    setTimeout(() => {
      console.log('Task 2 finished');
      resolve('Result 2');
    }, 1000)
  );
}

function testFunction() {
  task1(); // Will run in parallel
  task2();
  console.log('Both tasks started');
}

export { blockingFunction, testFunction };

