# Stage 1: Use jenkins inbound-agent base image to get jenkins-agent binaries
FROM jenkins/inbound-agent:latest as jnlp

# Stage 2: Ubuntu 18.04 base image to install required packages
FROM ubuntu:18.04

# Set environment variables to prevent interactive prompts during package installation
ENV DEBIAN_FRONTEND=noninteractive

# Install required packages and OpenJDK 17
RUN apt-get update && \
    apt-get install -y \
    git-core gnupg flex bison build-essential zip libssl-dev cmake curl zlib1g-dev \
    libc6-dev-i386 libncurses5 lib32ncurses5-dev x11proto-core-dev libx11-dev lib32z1-dev \
    libgl1-mesa-dev libxml2-utils xsltproc unzip fontconfig vim gcc-multilib g++-multilib \
    libpopt-dev rsync python-minimal python3-minimal python-pip git-lfs jq pigz wget openjdk-17-jre-headless \
    dnsutils iputils-ping curl net-tools iproute2 \
    ruby-full && \
    gem install nokogiri -v 1.12.5 && \
    gem install roo -v 2.8.3 && \
    curl https://storage.googleapis.com/git-repo-downloads/repo-1 > /usr/local/bin/repo && \
    chmod a+x /usr/local/bin/repo

# Set up user creation process with argumentized username and password
ARG USERNAME
ARG USERPASSWD
RUN if [ "$USERNAME" = "scm" ]; then \
      groupadd -g 1001 ${USERNAME} && \
      useradd -m -u 1001 -g 1001 -o -s /bin/bash ${USERNAME} && \
      mkdir -p /workspaces/jenkins; \
    else \
      useradd -ms /bin/bash ${USERNAME:-dev}; \
    fi
RUN echo "${USERNAME:-dev}:${USERPASSWD:-root}" | chpasswd

# Copy Jenkins agent files from the first stage (jnlp)
COPY --from=jnlp /usr/local/bin/jenkins-agent /usr/local/bin/jenkins-agent
COPY --from=jnlp /usr/share/jenkins/agent.jar /usr/share/jenkins/agent.jar

# Define entrypoint for the container
ENTRYPOINT ["/usr/local/bin/jenkins-agent"]

