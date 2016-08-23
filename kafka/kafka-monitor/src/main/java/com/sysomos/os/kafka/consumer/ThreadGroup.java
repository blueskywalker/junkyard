package com.sysomos.os.kafka.consumer;

import com.google.common.collect.Lists;
import org.apache.log4j.Logger;

import java.util.List;
import java.util.concurrent.atomic.AtomicBoolean;

/**
 * Created by kkim on 5/3/16.
 */
public class ThreadGroup {

    public static Logger logger = Logger.getLogger(ThreadGroup.class);

    protected final List<Thread> workers;



    public ThreadGroup() {
        workers = Lists.newArrayList();
    }

    public ThreadGroup(List<Runnable> runners) {
        this();
        addWorker(runners);
    }

    public void addWorker(List<Runnable> rs) {
        for(Runnable r: rs) {
            workers.add(new Thread(r));
        }
    }

    public void addWorker(Runnable... rs) {
        addWorker(rs);
    }

    public void start() {
        for (Thread t : workers) {
            if (t != null) {
                t.start();
            }
        }
    }

    public void join() throws InterruptedException {
        for (Thread t : workers) {
            if (t != null) {
                t.join();

            }
        }
    }

    public void shutdown() throws InterruptedException {
        for (Thread t : workers) {
            if (t != null) {
                t.interrupt();
            }
        }
    }

}
