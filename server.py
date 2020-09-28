from concurrent import futures
import logging
import numpy as np

import grpc

import test_pb2
import test_pb2_grpc


class Transit(test_pb2_grpc.TransitServicer):

    def GetString(self, request, context):
        return test_pb2.StringReply(message='this is string from server')
        #return test_pb2.StringReply(message='a'*1000000)
    
    def GetNum(self,request, context):
        y = twosum(request.x1, request.x2)
        
        return test_pb2.NumReply(y=y)
    
    def GetList(self, request, context):
        i = request.ind
        select_list = select_array(i)
        return test_pb2.ListReply(ListReply=select_list)
   



def twosum(x1,x2):
    return x1+x2

def select_array(ind):
    a = np.random.rand(100,5)
    return a[ind].tolist()


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    test_pb2_grpc.add_TransitServicer_to_server(Transit(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()

