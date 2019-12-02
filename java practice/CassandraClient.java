//import com.datastax.driver.core.Session;
//
//import java.io.File;
//import java.util.Scanner;
//import java.lang.reflect.Method;
//import java.lang.reflect.*;
//import org.apache.logging.log4j.*;
//import org.junit.Assert;
//
//
///**
// * @author shahrozimtiaz
// */
//public class CassandraClient {
//    private static Scanner scan;
//    private static Scanner filer;
//    private static String input;
//    private static String[] inputs;
//    private static String methodName;
//    private static String[] arguments;
//    private static String argument;
//    private static Method method;
//
////    private static final Logger log = LogManager.getLogger();
//    public static void main(String[] args) {
//        print("Starting...");
//        CassConnect connector = new CassConnect();
//        connector.connect("127.0.0.1",null);
//        Session session = connector.getSession();
//        connector.close();
//        print("Finished...");
////        scan = new Scanner(System.in);
////        while(true) {
////            print("Enter 1 for command line input. Enter 2 for batch file input. Enter 3 to exit.");
////            input = scan.nextLine();
////            if (input.equals("2")) { //batch file
////                while (true){
////                    try {
////                        print("Enter file path");
////                        String fileName = scan.nextLine();
////                        filer = new Scanner(new File(fileName));
////                         break;
////                    }catch (Exception e){
////                        print("File not found.");
////                    }
////                }
////                while(filer.hasNextLine()){
////                    input = filer.nextLine();
////                    query();
////                }
////
////            } else if (input.equals("1")) { //command line
////                while (true) {
////                    input = prompt().toUpperCase();
////                    if(input.equals("EXIT")){
////                        print("Now exiting..");
////                        System.exit(0);
////                    }else {
////                        query();
////                    }
////                }
////            } else if(input.equals("3")) {
////                print("Now exiting..");
////                System.exit(0);
////            } else{
////                print("Invalid input.");
////            }
////        }
//    }
//
//    /**
//     * This invokes the method/command that was given.
//     */
//    public static void query(){
//            inputs = input.split(" ");
//            methodName = inputs[0];
//            arguments = new String[inputs.length-1];
//            for(int i =1; i < inputs.length;i++){
//                arguments[i-1] = inputs[i];
//            }
//            if(arguments.length>0) {
//                argument = arguments[0];
//            }
//
//            try {
//                method = CassandraClient.class.getMethod(methodName, String.class);
//            }
//            catch (SecurityException e) {
//                print("Failed due to security");
//                System.exit(9);
//            }
//            catch (NoSuchMethodException e) {
//                print("No such Method. Try again.");
//                return;
//            }
//
//            try {
//                String response = String.valueOf(method.invoke(methodName, argument));
//                print(response);
//
//            }
//            catch (IllegalArgumentException e) {
//                print("Illegal Argument");
//                System.exit(1);
//            }
//            catch (IllegalAccessException e) {
//                print("Illegal Access");
//                System.exit(1);
//            }
//            catch (InvocationTargetException e) {
//                print("target error");
//                System.exit(1);
//            }
//    }
//
//    /**
//     * y code to iso
//     * @param  ycpy The y code.
//     * @return This method returns the iso code for the given y code.
//     */
//    //Test Ycpy = ERP , ISO = ABE
//    public static String GET_YCPY_ISO(String ycpy){
////        ServiceAttributeRulesMapper map = new ServiceAttributeRulesMapper();
////        List<SerivceAttributeRules> rows = map.get("gpi","ycopy_service_code_participant");
////        for(ServiceAttributeRules row : rows){
////            if(row.getAtributeValue1.equals(ycpy)){
////                Assert.assertEquals(row.getAtributeValue2, "ABE");
////                return row.getAtributeValue2;
////            }
////        }
//        String result = "ABZ";
////        Assert.assertEquals(result, "ABE");
//
//        return "found code for:" + ycpy;
////        return "Error: Query not found.";
//    }
//
//
//    /**
//     * v code to iso
//     * @param vcpy The v code.
//     * @return  This method returns iso code for the given v code.
//     */
//    //Test vcpy = BOTHTHBK , ISO = THB
//    public static String GET_VCPY_ISO(String vcpy){
////        ServiceAttributeRulesMapper map = new ServiceAttributeRulesMapper();
////        List<SerivceAttributeRules> rows = map.get("gpi","vcopy_service_code_participant");
////        for(ServiceAttributeRules row : rows){
////            if(row.getAtributeValue1.equals(vcpy)){
////                Assert.assertEquals(row.getAtributeValue2, "THB");
////                return row.getAtributeValue2;
////            }
////        }
//        String result = "THC";
////        Assert.assertEquals(result, "THB");
//        return "found code for:" + vcpy;
//
////        return "Error: Query not found.";
//    }
//
//    /**
//     * Simple print method to quickly print Object.
//     * @param o
//     */
//    private static void print(Object o){
//        System.out.println(o);
//    }
//
//    /**
//     * This method prompts the user for a command and grabs the response
//     * @return User's response
//     */
//    private static String prompt(){
//        print("Please enter a command");
//        return scan.nextLine();
//    }
//}