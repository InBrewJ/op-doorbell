package com.urawizard;

import java.io.IOException;
import java.io.PrintWriter;
import java.util.concurrent.TimeoutException;

import javax.servlet.ServletException;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

public class Server extends HttpServlet {
    public void doGet(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {

        response.setContentType("text/event-stream");
        response.setCharacterEncoding("UTF-8");

        PrintWriter writer = response.getWriter();
        try {
            Consumer consumer = new Consumer();
            boolean error = false;
            while (!error) {
                Thread.sleep(500);
                if (consumer.hasMessages()) {
                    writer.write("data: " + consumer.getLastMessage() + "\n\n");
                    error = writer.checkError(); // internally calls writer.flush()
                }
            }
            writer.close();
            consumer.destroy();
        } catch (TimeoutException | InterruptedException e) {
            e.printStackTrace();
        }
    }
}
