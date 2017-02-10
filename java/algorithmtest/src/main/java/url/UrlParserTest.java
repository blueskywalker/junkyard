package url;

import java.net.MalformedURLException;
import java.net.URI;
import java.net.URISyntaxException;
import java.net.URL;
import java.util.HashSet;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

/**
 * Created by jerrykim on 12/14/16.
 */
public class UrlParserTest {

    public final static String regex = "((https?)://)?([^/]+)/?(.*)";
    public final static Pattern pattern = Pattern.compile(regex);

    public static String getTopDomain(String host) {
        if (host != null && host.startsWith("www."))
            return host.substring(4);

        return host;
    }

    static final HashSet<String> topLevelDomain = new HashSet<>();

    static {
        topLevelDomain.add("com");
        topLevelDomain.add("biz");
        topLevelDomain.add("mobi");
        topLevelDomain.add("travel");
        topLevelDomain.add("net");
        topLevelDomain.add("info");
        topLevelDomain.add("pw");
        topLevelDomain.add("tv");
        topLevelDomain.add("org");
        topLevelDomain.add("int");
        topLevelDomain.add("tel");
        topLevelDomain.add("XXX");
    }

    public static String getCompanyNameFromDomain(String domain) {

        if (domain != null && domain.length() > 0) {
            String host = parse(domain);
            if (host == null) {
                System.out.println("debug");
            }
            String[] parts = host.split("\\.");
            if (parts.length == 2)
                return parts[0];

            if (!topLevelDomain.contains(parts[parts.length - 1])) {
                if (parts.length > 2) {
                    return parts[parts.length - 3];
                }
            } else {
                return parts.length>1?parts[parts.length-2]:"";
            }
        }
        return "";
    }

    public static String parse(String url) {
        Matcher matcher = pattern.matcher(url);
        if (matcher.find()) {
            return matcher.group(3);
        }
        return null;
    }

    public static void main(String[] args) {
        String url = "https://www.ibm.com/developerworks/downloads/ws/worklight/";

        System.out.println(getCompanyNameFromDomain(url));
    }
}
