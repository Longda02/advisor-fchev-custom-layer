clear;clc
if count(py.sys.path,'') == 0
    insert(py.sys.path,int32(0),'');
end
% py.print('ajghshdgaskj')
b = py.Network.NetworkInput(0.6, 0.6, 20, 15.5, 0.6);
% b = py.add.add(3,5);
% clear classes
% mod = py.importlib.import_module('example')
% py.importlib.reload(mod)
% py.example.add(2, 4)


