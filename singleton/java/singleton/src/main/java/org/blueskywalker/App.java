package org.blueskywalker;

/**
 * Hello world!
 *
 */
public class App
{
    public static void main( String[] args )
    {
       for(int i=0;i<20;i++) {
           new Thread(new Runnable() {
               public void run() {
                   System.out.println(Singleton.getInstance());
               }
           }).start();
       }
    }
}
