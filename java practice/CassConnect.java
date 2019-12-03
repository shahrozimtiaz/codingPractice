//import com.datastax.driver.core.*;
//import com.datastax.driver.core.Cluster.Builder;
//
//import java.util.Collection;
//
//public class CassConnect {
//    private Cluster cluster;
//    private Session session;
//
//    public void connect(String node, Integer port){
//        Builder b = Cluster.builder().addContactPoint(node);
//        if (port !=null){
//            b.withPort(port);
//        }
//        cluster = b.build();
//
////        Metadata metadata = cluster.getMetadata();
////        print("-----------------------------------------------------------");
////        print("-----------------------------------------------------------");
////        print("");
////
////        Collection<TableMetadata> list = metadata.getKeyspace("test_keyspace").getTables();
////        for(Object t : list){
////            print(t);
////        }
////
////        print("-----------------------------------------------------------");
////        print("-----------------------------------------------------------");
////        print("");
//
//
//        session = cluster.connect();
//    }
//    public Session getSession() {
//        return this.session;
//    }
//
//    public void close() {
//        session.close();
//        cluster.close();
//    }
//    public static void print(Object o){
//        System.out.println(o);
//    }
//}