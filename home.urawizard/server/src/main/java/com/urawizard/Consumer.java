package com.urawizard;

import com.rabbitmq.client.Channel;
import com.rabbitmq.client.Connection;
import com.rabbitmq.client.ConnectionFactory;
import com.rabbitmq.client.DeliverCallback;

import java.io.IOException;
import java.util.LinkedList;
import java.util.concurrent.TimeUnit;
import java.util.concurrent.TimeoutException;

public class Consumer {
    private final static String QUEUE_NAME = "t_wizard_mon";
    private final static String HOST = "eggs.urawizard.com";
    private Channel channel;
    private Connection connection;
    private LinkedList<String> messages = new LinkedList<String>();

    Consumer() throws IOException, TimeoutException {
        ConnectionFactory factory = new ConnectionFactory();
        factory.setHost(HOST);
        this.connection = factory.newConnection();
        this.channel = connection.createChannel();
        channel.queueDeclare(QUEUE_NAME, false, false, false, null);
        channel.basicQos(30);
        DeliverCallback deliverCallback = (consumerTag, delivery) -> {
            String message = new String(delivery.getBody(), "UTF-8");
            messages.add(message);
            try {
                TimeUnit.MILLISECONDS.sleep(750);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }

        };
        channel.basicConsume(QUEUE_NAME, false, deliverCallback, consumerTag -> {
        });
        System.out.println("Consumer setup complete");
    }

    public String getLastMessage() {
        String lastMessage = messages.getLast();
        messages.removeLast();
        return lastMessage;
    }

    public boolean hasMessages() {
        return !messages.isEmpty();
    }

    public void destroy() throws IOException, TimeoutException {
        System.out.println("Consumer destroyed");
        this.channel.close();
        this.connection.close();
    }

    public static void main(String[] argv) throws Exception {
        ConnectionFactory factory = new ConnectionFactory();
        factory.setHost(HOST);
        Connection connection = factory.newConnection();
        Channel channel = connection.createChannel();

        channel.queueDeclare(QUEUE_NAME, false, false, false, null);
        System.out.println(" [*] Waiting for messages. To exit press CTRL+C");

        DeliverCallback deliverCallback = (consumerTag, delivery) -> {
            String message = new String(delivery.getBody(), "UTF-8");
            System.out.println(" [x] Received '" + message + "'");
            try {
                TimeUnit.MILLISECONDS.sleep(250);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }

        };
        channel.basicConsume(QUEUE_NAME, true, deliverCallback, consumerTag -> {
        });
    }
}
