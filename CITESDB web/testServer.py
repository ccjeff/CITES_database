import eventlet
import socketio

sio = socketio.Server()
# the index.html file hosted by eventlet is a dummy file
# it appears to be required to host some html file.. 
app = socketio.WSGIApp(sio, static_files={
    '/static': './public'
})

@sio.on('connect')
def connect(sid, environ):
    print('connect ', sid)

@sio.on('value2server')
def value2server(sid, data):
    print('aaa')
    print(sid, data)

@sio.emit('notifyFinished',{'data': 'foobar'})
# def timer(sid, data):
#     print('message ', data)
#     sio.emit('timer', 2020)

@sio.on('disconnect')
def disconnect(sid):
    print('disconnect ', sid)

if __name__ == '__main__':
    eventlet.wsgi.server(eventlet.listen(('', 5000)), app)