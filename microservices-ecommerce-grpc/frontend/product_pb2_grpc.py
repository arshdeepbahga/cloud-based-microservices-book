# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import product_pb2 as product__pb2


class ProductServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetProducts = channel.unary_unary(
                '/ProductService/GetProducts',
                request_serializer=product__pb2.Empty.SerializeToString,
                response_deserializer=product__pb2.ProductList.FromString,
                )
        self.GetProduct = channel.unary_unary(
                '/ProductService/GetProduct',
                request_serializer=product__pb2.ProductRequest.SerializeToString,
                response_deserializer=product__pb2.Product.FromString,
                )
        self.GetProductWithID = channel.unary_unary(
                '/ProductService/GetProductWithID',
                request_serializer=product__pb2.ProductRequestID.SerializeToString,
                response_deserializer=product__pb2.Product.FromString,
                )
        self.CreateProduct = channel.unary_unary(
                '/ProductService/CreateProduct',
                request_serializer=product__pb2.ProductCreateRequest.SerializeToString,
                response_deserializer=product__pb2.Product.FromString,
                )


class ProductServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetProducts(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetProduct(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetProductWithID(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateProduct(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ProductServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetProducts': grpc.unary_unary_rpc_method_handler(
                    servicer.GetProducts,
                    request_deserializer=product__pb2.Empty.FromString,
                    response_serializer=product__pb2.ProductList.SerializeToString,
            ),
            'GetProduct': grpc.unary_unary_rpc_method_handler(
                    servicer.GetProduct,
                    request_deserializer=product__pb2.ProductRequest.FromString,
                    response_serializer=product__pb2.Product.SerializeToString,
            ),
            'GetProductWithID': grpc.unary_unary_rpc_method_handler(
                    servicer.GetProductWithID,
                    request_deserializer=product__pb2.ProductRequestID.FromString,
                    response_serializer=product__pb2.Product.SerializeToString,
            ),
            'CreateProduct': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateProduct,
                    request_deserializer=product__pb2.ProductCreateRequest.FromString,
                    response_serializer=product__pb2.Product.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'ProductService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class ProductService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetProducts(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ProductService/GetProducts',
            product__pb2.Empty.SerializeToString,
            product__pb2.ProductList.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetProduct(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ProductService/GetProduct',
            product__pb2.ProductRequest.SerializeToString,
            product__pb2.Product.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetProductWithID(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ProductService/GetProductWithID',
            product__pb2.ProductRequestID.SerializeToString,
            product__pb2.Product.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CreateProduct(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ProductService/CreateProduct',
            product__pb2.ProductCreateRequest.SerializeToString,
            product__pb2.Product.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)