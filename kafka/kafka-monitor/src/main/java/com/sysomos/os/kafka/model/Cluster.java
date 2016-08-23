package com.sysomos.os.kafka.model;

import com.fasterxml.jackson.annotation.JsonProperty;
import org.apache.commons.lang3.builder.EqualsBuilder;
import org.apache.commons.lang3.builder.HashCodeBuilder;
import org.apache.commons.lang3.builder.ToStringBuilder;


/**
 * Created by kkim on 4/27/16.
 */
public class Cluster extends BaseModel {

    private String name;
    private String zookeeper;

    public Cluster() {
    }

    public Cluster(String name, String zookeeper) {
        this.name = name;
        this.zookeeper = zookeeper;
    }

    @JsonProperty
    public String getName() {
        return name;
    }

    @JsonProperty
    public String getZookeeper() {
        return zookeeper;
    }

    @JsonProperty
    public void setName(String name) {
        this.name = name;
    }
    @JsonProperty
    public void setZookeeper(String zookeeper) {
        this.zookeeper = zookeeper;
    }


    @Override
    public boolean equals(Object obj) {
        if (obj == null) {
            return false;
        }
        if (obj == this) {
            return true;
        }
        if (obj.getClass() != getClass()) {
            return false;
        }
        Cluster rhs = (Cluster) obj;
        return new EqualsBuilder()
                .append(this.name, rhs.name)
                .append(this.zookeeper, rhs.zookeeper)
                .isEquals();
    }

    @Override
    public int hashCode() {
        return new HashCodeBuilder()
                .append(name)
                .append(zookeeper)
                .toHashCode();
    }


    @Override
    public String toString() {
        return new ToStringBuilder(this)
                .appendSuper(super.toString())
                .append("name", name)
                .append("zookeeper", zookeeper)
                .toString();
    }
}
