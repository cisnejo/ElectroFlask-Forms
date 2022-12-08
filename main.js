const { app, BrowserWindow } = require('electron')
const path = require('path')
const {PythonShell}  = require ('python-shell');


let options = {
    mode: 'text',
    pythonPath: './venv/Scripts/python.exe',
    pythonOptions: ['-u'], // get print results in real-time

  };

function createWindow() {
    /* Spawn a child process for development */
    PythonShell.run('./app.py', options, function (err, results) {
        if (err) throw err;
        // results is an array consisting of messages collected during execution
        console.log('results: %j', results);
      });

    /* End spawn */
    
    const win = new BrowserWindow({
        width: 800,
        height: 600,
        webPreferences: {
            preload: path.join(__dirname, 'preload.js')
        }
    })

    win.loadFile('index.html')
}

app.whenReady().then(() => {
    createWindow()

    app.on('activate', () => {
        if (BrowserWindow.getAllWindows().length === 0) {
            createWindow()
        }
    })
})

app.on('window-all-closed', () => {
    if (process.platform !== 'darwin') {
        app.quit()
    }
})
