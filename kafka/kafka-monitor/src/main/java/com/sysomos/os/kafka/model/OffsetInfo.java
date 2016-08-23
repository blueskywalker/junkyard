package com.sysomos.os.kafka.model;

import com.fasterxml.jackson.annotation.JsonInclude;
import com.fasterxml.jackson.annotation.JsonProperty;
import org.apache.commons.lang3.builder.ToStringBuilder;

/**
 * Created by kkim on 5/3/16.
 */


public class OffsetInfo  extends BaseModel {

    @JsonProperty
    private String topic;

    @JsonInclude(JsonInclude.Include.NON_NULL)
    @JsonProperty
    private Integer partition;
    @JsonProperty
    private Long offset;
    @JsonProperty
    private Long logsize;
    @JsonProperty
    private Long lag;
    @JsonProperty
    private Integer timestamp; //utc


    public OffsetInfo(String topic, Integer partition, Long offset, Long logsize, Long lag, Integer timestamp) {
        this.topic = topic;
        this.partition = partition;
        this.offset = offset;
        this.logsize = logsize;
        this.lag = lag;
        this.timestamp = timestamp;
    }

    public String getTopic() {
        return topic;
    }

    public void setTopic(String topic) {
        this.topic = topic;
    }

    public Integer getPartition() {
        return partition;
    }

    public void setPartition(Integer partition) {
        this.partition = partition;
    }

    public Long getOffset() {
        return offset;
    }

    public void setOffset(Long offset) {
        this.offset = offset;
    }

    public Long getLogsize() {
        return logsize;
    }

    public void setLogsize(Long logsize) {
        this.logsize = logsize;
    }

    public Long getLag() {
        return lag;
    }

    public void setLag(Long lag) {
        this.lag = lag;
    }

    public Integer getTimestamp() {
        return timestamp;
    }

    public void setTimestamp(Integer timestamp) {
        this.timestamp = timestamp;
    }


    @Override
    public String toString() {
        return new ToStringBuilder(this)
                .appendSuper(super.toString())
                .append("topic", topic)
                .append("partition", partition)
                .append("offset", offset)
                .append("logsize", logsize)
                .append("lag", lag)
                .append("timestamp", timestamp)
                .toString();
    }
}
