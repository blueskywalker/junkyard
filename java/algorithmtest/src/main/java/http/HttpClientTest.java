package http;

import com.google.common.base.Charsets;
import com.google.common.io.CharStreams;
import org.apache.http.HttpResponse;
import org.apache.http.client.HttpClient;
import org.apache.http.client.methods.HttpGet;
import org.apache.http.client.utils.URIBuilder;
import org.apache.http.impl.client.HttpClientBuilder;


import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.StringWriter;
import java.net.URI;
import java.net.URISyntaxException;
import java.nio.charset.Charset;
import java.nio.charset.StandardCharsets;

/**
 * Created by jerrykim on 2/13/17.
 */
public class HttpClientTest {

    private final String captoraToken = "X-CAPTORA-TOKEN";
    private final String token = "APIKEY-ac6d68f24c46ea8cdcff4bbe8e330091";
    private final String contentType = "content-type";
    private final String json = "application/json";
    private final String endpoint;

    public HttpClientTest() {
        this.endpoint = String.format("http://%s:%d/demand-manager-plus","54.193.212.95",8080);
    }

    public String getOrganicGroups(String account) throws IOException {
        final String api = String.format("%s/%s/demand-family",endpoint,account);

        HttpClient client = HttpClientBuilder.create().build();

        HttpGet get = new HttpGet(api);

        get.setHeader(captoraToken,token);
        get.setHeader(contentType,json);

        HttpResponse response = client.execute(get);

        return CharStreams.toString( new InputStreamReader(response.getEntity().getContent(),
                Charsets.UTF_8));
    }

    public String getOrganicGroup(String account,String group) throws IOException, URISyntaxException {
        final String api = String.format("%s/%s/demand-family",endpoint,account);

        HttpClient client = HttpClientBuilder.create().build();

        URI url = new URIBuilder(api)
                .addParameter("search-on","name")
                .addParameter("search-term",group)
                .build();

        HttpGet get = new HttpGet(url);

        get.setHeader(captoraToken,token);
        get.setHeader(contentType,json);

        HttpResponse response = client.execute(get);

        return CharStreams.toString( new InputStreamReader(response.getEntity().getContent(),
                Charsets.UTF_8));
    }

    public static void main(String[] args) {
        HttpClientTest service = new HttpClientTest();

        try {
            System.out.println(service.getOrganicGroup("acquia.com","intellectual property"));
        } catch (IOException e) {
            e.printStackTrace();
        } catch (URISyntaxException e) {
            e.printStackTrace();
        }
    }
}
