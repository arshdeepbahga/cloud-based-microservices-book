# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import order_pb2 as order__pb2


class OrderServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.AddItem = channel.unary_unary(
                '/order.OrderService/AddItem',
                request_serializer=order__pb2.AddItemRequest.SerializeToString,
                response_deserializer=order__pb2.OrderResponse.FromString,
                )
        self.GetOrder = channel.unary_unary(
                '/order.OrderService/GetOrder',
                request_serializer=order__pb2.GetOrderRequest.SerializeToString,
                response_deserializer=order__pb2.OrderResponse.FromString,
                )
        self.Checkout = channel.unary_unary(
                '/order.OrderService/Checkout',
                request_serializer=order__pb2.CheckoutRequest.SerializeToString,
                response_deserializer=order__pb2.OrderResponse.FromString,
                )
        self.GetCart = channel.unary_unary(
                '/order.OrderService/GetCart',
                request_serializer=order__pb2.GetCartRequest.SerializeToString,
                response_deserializer=order__pb2.GetCartResponse.FromString,
                )
        self.GetOrders = channel.unary_unary(
                '/order.OrderService/GetOrders',
                request_serializer=order__pb2.GetOrdersRequest.SerializeToString,
                response_deserializer=order__pb2.GetOrdersResponse.FromString,
                )


class OrderServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def AddItem(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetOrder(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Checkout(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetCart(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetOrders(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_OrderServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'AddItem': grpc.unary_unary_rpc_method_handler(
                    servicer.AddItem,
                    request_deserializer=order__pb2.AddItemRequest.FromString,
                    response_serializer=order__pb2.OrderResponse.SerializeToString,
            ),
            'GetOrder': grpc.unary_unary_rpc_method_handler(
                    servicer.GetOrder,
                    request_deserializer=order__pb2.GetOrderRequest.FromString,
                    response_serializer=order__pb2.OrderResponse.SerializeToString,
            ),
            'Checkout': grpc.unary_unary_rpc_method_handler(
                    servicer.Checkout,
                    request_deserializer=order__pb2.CheckoutRequest.FromString,
                    response_serializer=order__pb2.OrderResponse.SerializeToString,
            ),
            'GetCart': grpc.unary_unary_rpc_method_handler(
                    servicer.GetCart,
                    request_deserializer=order__pb2.GetCartRequest.FromString,
                    response_serializer=order__pb2.GetCartResponse.SerializeToString,
            ),
            'GetOrders': grpc.unary_unary_rpc_method_handler(
                    servicer.GetOrders,
                    request_deserializer=order__pb2.GetOrdersRequest.FromString,
                    response_serializer=order__pb2.GetOrdersResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'order.OrderService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class OrderService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def AddItem(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/order.OrderService/AddItem',
            order__pb2.AddItemRequest.SerializeToString,
            order__pb2.OrderResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetOrder(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/order.OrderService/GetOrder',
            order__pb2.GetOrderRequest.SerializeToString,
            order__pb2.OrderResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Checkout(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/order.OrderService/Checkout',
            order__pb2.CheckoutRequest.SerializeToString,
            order__pb2.OrderResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetCart(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/order.OrderService/GetCart',
            order__pb2.GetCartRequest.SerializeToString,
            order__pb2.GetCartResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetOrders(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/order.OrderService/GetOrders',
            order__pb2.GetOrdersRequest.SerializeToString,
            order__pb2.GetOrdersResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
