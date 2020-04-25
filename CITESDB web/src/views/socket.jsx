import openSocket from 'socket.io-client';
const  socket = openSocket('http://localhost:5000');

export function subscribeToTimer(cb) {
  socket.on('timer', timestamp => cb(null, timestamp));
  socket.emit('subscribeToTimer', 1000);
}

export function sendToServer(val){
    socket.emit('value2server',val);
}

export default { subscribeToTimer, sendToServer};