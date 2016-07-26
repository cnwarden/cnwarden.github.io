---
layout: post_mine
title:  machine learning
---

K-Means

说收敛慢的那个注意下kmeans业界用得多的原因之一就是收敛快，现在还能通过分布式计算加速，别的原因有调参就一个K。
缺点大把，其实聚类这种non-supervised 的东西一只被人们诟病。
1. 调K。虽然只用调一个参数，但是clustering的几个metrics，gap statistic，silhouette statistic，算起来都很慢，很慢很慢。
2. Kmeans 其实是在做convex optimization ，遇到non-convex 的distribution 就挂了。怎么办？加Kernel 。加什么Kernel 慢慢试吧，svm用什么Kernel好不就是这一个个试出来的嘛。
3. 不怎么robust ，所以就出现KMedians,KMedoid 这种更慢的东西。
4. Hidden class highly imbalanced 的时候效果不好。这个自己造几个数据试试就知道了。
5. 收敛到局部最优，类似EM。要算好多好多次~

- [1](https://www.zhihu.com/question/31296149)
