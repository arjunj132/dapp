console.log(`
██████   █████  ██████  ██████  
██   ██ ██   ██ ██   ██ ██   ██ 
██   ██ ███████ ██████  ██████  
██   ██ ██   ██ ██      ██      
██████  ██   ██ ██      ██      

(c) Arjun J
`);
function start() {
    executable = document.getElementsByClassName('exe')[0].value
    code = document.getElementsByClassName('code')[0].value
    const spawn = require("child_process").spawn;
    const pythonProcess = spawn(executable,["app.py", code]);
    pythonProcess.stdout.on('data', (data) => {
        data = data.toString()
        console.log(data)
    });
}