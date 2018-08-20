import java.awt.Robot;
import java.awt.event.KeyEvent;

public class Keypress {
  // Press
  public static void press(String keystring) {
    int key = Integer.parseInt(keystring);
    try {
      Robot robot = new Robot();
      // Cases
      switch(key) {
        case 97 :
        robot.keyPress(KeyEvent.VK_A);
        //robot.delay(10);
        break;
        case 98 :
        robot.keyPress(KeyEvent.VK_B);
        //robot.delay(10);
        break;
        case 99 :
        robot.keyPress(KeyEvent.VK_C);
        //robot.delay(10);
        break;
        case 100 :
        robot.keyPress(KeyEvent.VK_D);
        //robot.delay(10);
        break;
        case 101 :
        robot.keyPress(KeyEvent.VK_E);
        //robot.delay(10);
        break;
        case 102 :
        robot.keyPress(KeyEvent.VK_F);
        //robot.delay(10);
        break;
        case 103 :
        robot.keyPress(KeyEvent.VK_G);
        //robot.delay(10);
        break;
        case 104 :
        robot.keyPress(KeyEvent.VK_H);
        //robot.delay(10);
        break;
        case 105 :
        robot.keyPress(KeyEvent.VK_I);
        //robot.delay(10);
        break;
        case 106 :
        robot.keyPress(KeyEvent.VK_J);
        //robot.delay(10);
        break;
        case 107 :
        robot.keyPress(KeyEvent.VK_K);
        //robot.delay(10);
        break;
        case 108 :
        robot.keyPress(KeyEvent.VK_L);
        //robot.delay(10);
        break;
        case 109 :
        robot.keyPress(KeyEvent.VK_M);
        //robot.delay(10);
        break;
        case 110 :
        robot.keyPress(KeyEvent.VK_N);
        //robot.delay(10);
        break;
        case 111 :
        robot.keyPress(KeyEvent.VK_O);
        //robot.delay(10);
        break;
        case 112 :
        robot.keyPress(KeyEvent.VK_P);
        //robot.delay(10);
        break;
        case 113 :
        robot.keyPress(KeyEvent.VK_Q);
        //robot.delay(10);
        break;
        case 114 :
        robot.keyPress(KeyEvent.VK_R);
        //robot.delay(10);
        break;
        case 115 :
        robot.keyPress(KeyEvent.VK_S);
        //robot.delay(10);
        break;
        case 116 :
        robot.keyPress(KeyEvent.VK_T);
        //robot.delay(10);
        break;
        case 117 :
        robot.keyPress(KeyEvent.VK_U);
        //robot.delay(10);
        break;
        case 118 :
        robot.keyPress(KeyEvent.VK_V);
        //robot.delay(10);
        break;
        case 119 :
        robot.keyPress(KeyEvent.VK_W);
        //robot.delay(10);
        break;
        case 120 :
        robot.keyPress(KeyEvent.VK_X);
        //robot.delay(10);
        break;
        case 121 :
        robot.keyPress(KeyEvent.VK_Y);
        //robot.delay(10);
        break;
        case 122 :
        robot.keyPress(KeyEvent.VK_Z);
        //robot.delay(10);
        break;
        case 273 :
        robot.keyPress(KeyEvent.VK_UP);
        //robot.delay(10);
        break;
        case 274 :
        robot.keyPress(KeyEvent.VK_DOWN);
        //robot.delay(10);
        break;
        case 276 :
        robot.keyPress(KeyEvent.VK_LEFT);
        //robot.delay(10);
        break;
        case 275 :
        robot.keyPress(KeyEvent.VK_RIGHT);
        //robot.delay(10);
        break;
        case 27 :
        robot.keyPress(KeyEvent.VK_ESCAPE);
        //robot.delay(10);
        break;
        case 32 :
        robot.keyPress(KeyEvent.VK_SPACE);
        //robot.delay(10);
        break;
        case 13 :
        robot.keyPress(KeyEvent.VK_ENTER);
        //robot.delay(10);
        break;
        case 306 :
        robot.keyPress(KeyEvent.VK_CONTROL);
        //robot.delay(10);
        break;
        case 308 :
        robot.keyPress(KeyEvent.VK_ALT);
        //robot.delay(10);
        break;
        case 304 :
        robot.keyPress(KeyEvent.VK_SHIFT);
        //robot.delay(10);
        break;
        case 303 :
        robot.keyPress(KeyEvent.VK_SHIFT);
        //robot.delay(10);
        break;
        case 9 :
        robot.keyPress(KeyEvent.VK_TAB);
        //robot.delay(10);
        break;
        case 48 :
        robot.keyPress(KeyEvent.VK_0);
        //robot.delay(10);
        break;
        case 49 :
        robot.keyPress(KeyEvent.VK_1);
        //robot.delay(10);
        break;
        case 50 :
        robot.keyPress(KeyEvent.VK_2);
        //robot.delay(10);
        break;
        case 51 :
        robot.keyPress(KeyEvent.VK_3);
        //robot.delay(10);
        break;
        case 52 :
        robot.keyPress(KeyEvent.VK_4);
        //robot.delay(10);
        break;
        case 53 :
        robot.keyPress(KeyEvent.VK_5);
        //robot.delay(10);
        break;
        case 54 :
        robot.keyPress(KeyEvent.VK_6);
        //robot.delay(10);
        break;
        case 55 :
        robot.keyPress(KeyEvent.VK_7);
        //robot.delay(10);
        break;
        case 56 :
        robot.keyPress(KeyEvent.VK_8);
        //robot.delay(10);
        break;
        case 57 :
        robot.keyPress(KeyEvent.VK_9);
        //robot.delay(10);
        break;

      }
      // End Cases
    }
    catch(Exception e) {
      System.out.println("An Error Occured.");
    }
  }

  // Release
  public static void release(String keystring) {
    int key = Integer.parseInt(keystring);
    try {
      Robot robot = new Robot();
      // Cases
      switch(key) {
        case 97 :
        robot.keyRelease(KeyEvent.VK_A);
        break;
        case 98 :
        robot.keyRelease(KeyEvent.VK_B);
        break;
        case 99 :
        robot.keyRelease(KeyEvent.VK_C);
        break;
        case 100 :
        robot.keyRelease(KeyEvent.VK_D);
        break;
        case 101 :
        robot.keyRelease(KeyEvent.VK_E);
        break;
        case 102 :
        robot.keyRelease(KeyEvent.VK_F);
        break;
        case 103 :
        robot.keyRelease(KeyEvent.VK_G);
        break;
        case 104 :
        robot.keyRelease(KeyEvent.VK_H);
        break;
        case 105 :
        robot.keyRelease(KeyEvent.VK_I);
        break;
        case 106 :
        robot.keyRelease(KeyEvent.VK_J);
        break;
        case 107 :
        robot.keyRelease(KeyEvent.VK_K);
        break;
        case 108 :
        robot.keyRelease(KeyEvent.VK_L);
        break;
        case 109 :
        robot.keyRelease(KeyEvent.VK_M);
        break;
        case 110 :
        robot.keyRelease(KeyEvent.VK_N);
        break;
        case 111 :
        robot.keyRelease(KeyEvent.VK_O);
        break;
        case 112 :
        robot.keyRelease(KeyEvent.VK_P);
        break;
        case 113 :
        robot.keyRelease(KeyEvent.VK_Q);
        break;
        case 114 :
        robot.keyRelease(KeyEvent.VK_R);
        break;
        case 115 :
        robot.keyRelease(KeyEvent.VK_S);
        break;
        case 116 :
        robot.keyRelease(KeyEvent.VK_T);
        break;
        case 117 :
        robot.keyRelease(KeyEvent.VK_U);
        break;
        case 118 :
        robot.keyRelease(KeyEvent.VK_V);
        break;
        case 119 :
        robot.keyRelease(KeyEvent.VK_W);
        break;
        case 120 :
        robot.keyRelease(KeyEvent.VK_X);
        break;
        case 121 :
        robot.keyRelease(KeyEvent.VK_Y);
        break;
        case 122 :
        robot.keyRelease(KeyEvent.VK_Z);
        break;
        case 273 :
        robot.keyRelease(KeyEvent.VK_UP);
        break;
        case 274 :
        robot.keyRelease(KeyEvent.VK_DOWN);
        break;
        case 276 :
        robot.keyRelease(KeyEvent.VK_LEFT);
        break;
        case 275 :
        robot.keyRelease(KeyEvent.VK_RIGHT);
        break;
        case 27 :
        robot.keyRelease(KeyEvent.VK_ESCAPE);
        break;
        case 32 :
        robot.keyRelease(KeyEvent.VK_SPACE);
        break;
        case 13 :
        robot.keyRelease(KeyEvent.VK_ENTER);
        break;
        case 306 :
        robot.keyRelease(KeyEvent.VK_CONTROL);
        break;
        case 308 :
        robot.keyRelease(KeyEvent.VK_ALT);
        break;
        case 304 :
        robot.keyRelease(KeyEvent.VK_SHIFT);
        break;
        case 303 :
        robot.keyRelease(KeyEvent.VK_SHIFT);
        break;
        case 9 :
        robot.keyRelease(KeyEvent.VK_TAB);
        break;
        case 48 :
        robot.keyRelease(KeyEvent.VK_0);
        break;
        case 49 :
        robot.keyRelease(KeyEvent.VK_1);
        break;
        case 50 :
        robot.keyRelease(KeyEvent.VK_2);
        break;
        case 51 :
        robot.keyRelease(KeyEvent.VK_3);
        break;
        case 52 :
        robot.keyRelease(KeyEvent.VK_4);
        break;
        case 53 :
        robot.keyRelease(KeyEvent.VK_5);
        break;
        case 54 :
        robot.keyRelease(KeyEvent.VK_6);
        break;
        case 55 :
        robot.keyRelease(KeyEvent.VK_7);
        break;
        case 56 :
        robot.keyRelease(KeyEvent.VK_8);
        break;
        case 57 :
        robot.keyRelease(KeyEvent.VK_9);
        break;

      }
      // End Cases
    }
    catch(Exception e) {
      System.out.println("An Error Occured.");
    }
  }

  public static void main(String[] args){
    if (args[0].equals("Press")) {
      Keypress.press(args[1]);
    }
    else if (args[0].equals("Release")) {
      Keypress.release(args[1]);
    }
  }
}
