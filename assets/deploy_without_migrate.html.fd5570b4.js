import{_ as s,r as t,o as i,c as d,a as e,b as c,w as n,F as _,d as o,e as a}from"./app.f730fb15.js";const r={},u=e("p",null,"\u5728\u5B9E\u9645\u7684\u751F\u4EA7\u73AF\u5883\u7684\u90E8\u7F72\u8FC7\u7A0B\u4E2D\uFF0C\u56E2\u961F\u7684MySQL\u7684\u7BA1\u7406\u5458\u53EF\u80FD\u4E0D\u4F1A\u7ED9\u5230\u5E94\u7528\u8D26\u53F7create\u7B49\u6BD4\u8F83\u654F\u611F\u7684\u6743\u9650\uFF0C\u8FD9\u79CD\u60C5\u51B5\u4E0B\uFF0C\u6211\u4EEC\u53EF\u4EE5\u901A\u8FC7\u624B\u52A8\u8FC1\u79FB\u6570\u636E\u7684\u65B9\u5F0F\u8D77\u5230\u548C\u7B49\u540CDjango migrate\u7684\u6548\u679C\u3002",-1),h=e("p",null,"\u64CD\u4F5C\u6B65\u9AA4\uFF1A",-1),p=e("li",null,[o("\u8FDB\u5165Server\u670D\u52A1\u5DE5\u4F5C\u76EE\u5F55\u540E\uFF08\u5047\u8BBE\u5DE5\u4F5C\u76EE\u5F55\u4E3A "),e("code",null,"/data/CodeAnalysis/server/"),o("\uFF0C\u4EE5\u4E0B\u8DEF\u5F84\u5747\u4E3A\u5DE5\u4F5C\u76EE\u5F55\u5185\u7684\u76F8\u5BF9\u8DEF\u5F84\uFF09")],-1),S=o("\u5728\u5F00\u53D1\u73AF\u5883\u4E00\u4E2A\u6709\u5168\u90E8\u6743\u9650\u7684MySQL\u5730\u5740\uFF0C\u521D\u59CB\u5316\u6570\u636E\uFF08MySQL\u7248\u672C\u8FD0\u884C\u7248\u672C\uFF1A5.7\uFF09 "),m=o("\u6267\u884C"),g=e("code",null,"vi ./scripts/config.sh",-1),y=o("\uFF1A\u586B\u5199\u4E00\u4E2A\u6709\u5168\u90E8\u6743\u9650\u7684MySQL\u6570\u636E\u5E93\u5730\u5740\u548CRedis\u4FE1\u606F\u4EE5\u53CA\u6839\u636E\u9700\u8981\u8C03\u6574\u914D\u7F6E\u4FE1\u606F\uFF0C\u4E3B\u8981\u7684\u5DE5\u7A0B\u914D\u7F6E\u5DF2\u63D0\u4F9B\u9ED8\u8BA4\u503C\uFF0C\u5B57\u6BB5\u8BF4\u660E\u53EF\u4EE5\u67E5\u770B"),E=o("\u6587\u6863"),f=e("li",null,[o("\u6267\u884C"),e("code",null,"bash ./scripts/deploy.sh init"),o("\uFF1A\u521D\u59CB\u5316DB\u3001\u5B89\u88C5\u4F9D\u8D56\u548C\u8FD0\u884C\u521D\u59CB\u5316\u811A\u672C")],-1),v=e("li",null,[o("\u4F7F\u7528MySQLDump\u5DE5\u5177\u5BFC\u51FA\u8868\u7ED3\u6784\u4E0E\u6570\u636E\uFF1A"),e("code",null,"mysqldump -u user -p \u2013databases codedog_main codedog_analysis codedog_file codedog_login > codedog_all.sql")],-1),L=a("<li>\u5728\u751F\u4EA7\u73AF\u5883\u5EFA\u6570\u636E\u5E93\uFF0C\u8BE6\u60C5\u89C1\uFF1A<code>server/sql/init.sql</code></li><li>\u8FDE\u63A5MySQL\uFF0C\u5BFC\u5165\u6570\u636E\uFF1A <ul><li>\u4E34\u65F6\u5173\u95ED\u5916\u952E\u68C0\u67E5: <code>SET SESSION FOREIGN_KEY_CHECKS=0</code>\uFF0C\u5426\u5219\u4F1A\u56E0\u4E3A\u6570\u636E\u4E2D\u6709\u5916\u952E\u5173\u8054\u5BFC\u81F4\u5BFC\u5165\u5931\u8D25</li><li>\u5BFC\u5165\u8868\u7ED3\u6784\u4E0E\u6570\u636E: <code>source /youdir/codedog_all.sql;</code></li><li>\u5F00\u542F\u5916\u952E\u68C0\u67E5: <code>SET SESSION FOREIGN_KEY_CHECKS=1</code></li></ul></li><li>\u542F\u52A8\u670D\u52A1: \u76F4\u63A5\u6267\u884C <code>bash ./scripts/deploy.sh start</code>\uFF0C\u65E0\u9700\u6267\u884C <code>init</code>\u65B9\u6CD5\uFF0C\u5426\u5219\u4F1A\u5BFC\u81F4\u6570\u636E\u91CD\u590D\u5199\u5165</li>",3);function N(C,M){const l=t("RouterLink");return i(),d(_,null,[u,h,e("ol",null,[p,e("li",null,[S,e("ul",null,[e("li",null,[m,g,y,c(l,{to:"/zh/guide/server/"},{default:n(()=>[E]),_:1})]),f,v])]),L])],64)}var q=s(r,[["render",N],["__file","deploy_without_migrate.html.vue"]]);export{q as default};
