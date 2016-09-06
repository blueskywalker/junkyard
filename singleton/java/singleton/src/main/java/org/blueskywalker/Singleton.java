package org.blueskywalker;


import java.util.concurrent.locks.ReentrantLock;

public class Singleton {

    private static Singleton instance;

    private Singleton() {
    }

    // public Singleton getInstance() {
    //     if(instance==null) {
    //         synchronized(this) {
    //             if(instance==null)
    //                 instance = new Singleton();
    //         }
    //     }
    //     return instance;
    //}

    private final static ReentrantLock lock = new ReentrantLock();

    public static Singleton getInstance() {
        if(instance==null) {
            lock.lock();
            try {
                if(instance==null)
                    instance = new Singleton();
            } finally {
                lock.unlock();
            }
            System.out.printf("ID [%d] in lock\n",Thread.currentThread().getId());
            return instance;
        }
        System.out.printf("ID [%d]\n",Thread.currentThread().getId());
        return instance;
    }

}
