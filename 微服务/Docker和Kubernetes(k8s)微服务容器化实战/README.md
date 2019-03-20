- 什么是微服务
  - 特征
    - 单一职责
    - 轻量级通信(与平台 语言无关)
    - 隔离性
    - 业务数据独立
    - 技术多样性，提供API
- 微服务简单的示意图

- 优缺点
  - 优点
    - 独立性
    - 敏捷性
    - 技术栈灵活
    - 团队高效
  - 不足
   - 额外的工作，比如 划分微服务
   - 数据一致性
   - 沟通成本

- 微服务引入的问题
  - 微服务如何通信(重点)
    - 通信模式
    - 通信协议
      - REST API
      - RPC(重点) dubbo grpc thrift Motan
        - 如何选择RPC框架
          - 考虑点
            - IO 线程调度模型
            - 序列化
            - 多语言
            - 服务治理
          - 流行的RPC框架
            - dubbo
            - Motan
            - Thrift (支持多语言)
            - gRPC
            - 四个框架对比

      - MQ
  - 微服务如何发现彼此
    - 传统发现
    - 微服务发现

  - 微服务如何部署 更新 扩容
    - 服务编排 mesos docker swarn k8s
    - java语言  spring boot
    - springcloud 一系列框架，简化Java的分布式系统，springboot封装，是Java的微服务
      - springcloud核心组件
        - Netflix ribbon
        - Netflix hystrix
        - Netflix zuul

- 示例模式

- Thrift的安装与使用
  - 查看官网安装
  - 编译运行后检查端口，netstat -na|grep
