from __future__ import print_function

import logging
import grpc

import test_pb2
import test_pb2_grpc



def run():
    
    channel = grpc.insecure_channel('localhost:50051')
    stub = test_pb2_grpc.TransitStub(channel)
    
    
    string = stub.GetString(test_pb2.emptyparameter(something=""))
    print('get string: %s'%string.message)
    
    ans = stub.GetNum(test_pb2.NumRequest(x1=1.23, x2=4.56))
    print('sum of two num:',ans.y)
    
    response_list = stub.GetList(test_pb2.indexquery(ind=10))
    print('response_list',response_list.ListReply)


if __name__ == '__main__':
    logging.basicConfig()
    run()



