(function(){var t={6076:function(){},1102:function(){},4845:function(t,e,n){"use strict";n(6992),n(8674),n(9601),n(7727);var a=n(144),r=function(){var t=this,e=t.$createElement,n=t._self._c||e;return n("div",[n("div",{staticClass:"links"},[n("router-link",{staticClass:"eachLink",attrs:{to:"/"}},[t._v("ホーム")]),t._v("/ "),n("router-link",{staticClass:"eachLink",attrs:{to:"/explanation"}},[t._v("遊び方")])],1),n("router-view")],1)},o=[],s=n(6076),i=n.n(s),c=i(),l=n(1001),u=(0,l.Z)(c,r,o,!1,null,null,null),p=u.exports,f=n(8345),v=function(){var t=this,e=t.$createElement,n=t._self._c||e;return n("div",[n("h1",{staticClass:"title"},[t._v("ドン・ブラコッコ")]),n("button",{staticClass:"btn1",on:{click:function(e){t.postTimes(),t.QuestionPage()}}},[t._v("スタート")]),n("button",{staticClass:"btn2",on:{click:function(e){return t.ExplanationPage()}}},[t._v("遊び方")]),n("select",{directives:[{name:"model",rawName:"v-model",value:t.selectedTime,expression:"selectedTime"}],on:{change:function(e){var n=Array.prototype.filter.call(e.target.options,(function(t){return t.selected})).map((function(t){var e="_value"in t?t._value:t.value;return e}));t.selectedTime=e.target.multiple?n:n[0]}}},[n("option",[t._v("1")]),n("option",[t._v("2")]),n("option",[t._v("3")])])])},m=[],h=n(9669),d=n.n(h),_={data:function(){return{selectedTime:"1"}},methods:{QuestionPage:function(){this.$router.push("/question")},ExplanationPage:function(){this.$router.push("/explanation")},postTimes:function(){d().put("https://still-stream-18883.herokuapp.com/"+this.selectedTime).then((function(t){console.log(t.data)})).catch((function(t){return console.log(t)}))}}},g=_,b=(0,l.Z)(g,v,m,!1,null,"f70ab472",null),C=b.exports,w=function(){var t=this,e=t.$createElement,n=t._self._c||e;return n("div",{staticClass:"container"},[n("div",{staticClass:"question"},[n("p",[t._v("問題")]),n("p",[t._v(t._s(t.sample.translated))])]),n("div",{staticClass:"choices",attrs:{id:"choices"}},[t._v(" --\x3e "),n("router-link",{staticClass:"choice",attrs:{to:{name:"AnswerPage",params:{bool:!0,origin:t.sample.source,translated:t.sample.translated}}}},[t._v(t._s(t.sample.choices.correct)+" ")]),n("router-link",{staticClass:"choice",attrs:{to:{name:"AnswerPage",params:{bool:!1,origin:t.sample.source,translated:t.sample.translated}}}},[t._v(t._s(t.sample.choices.wrong[0])+" ")]),n("router-link",{staticClass:"choice",attrs:{to:{name:"AnswerPage",params:{bool:!1,origin:t.sample.source,translated:t.sample.translated}}}},[t._v(t._s(t.sample.choices.wrong[1])+" ")]),n("router-link",{staticClass:"choice",attrs:{to:{name:"AnswerPage",params:{bool:!1,origin:t.sample.source,translated:t.sample.translated}}}},[t._v(t._s(t.sample.choices.wrong[2])+" ")])],1)])},x=[],k={data:function(){return{sample:null}},mounted:function(){var t=this;d().get("https://still-stream-18883.herokuapp.com/").then((function(e){return t.sample=e.data})).catch((function(t){return console.log(t)}))},updated:function(){for(var t=document.getElementById("choices"),e=t.children.length;e>=0;e--)t.appendChild(t.children[Math.random()*e|0])}},P=k,$=(0,l.Z)(P,w,x,!1,null,"03f6798d",null),y=$.exports,O=function(){var t=this,e=t.$createElement,n=t._self._c||e;return n("div",{staticClass:"container"},[n("div",{staticClass:"judge"},[t.$route.params.bool?n("p",{staticClass:"correct"},[t._v("正解！")]):n("p",{staticClass:"wrong"},[t._v("不正解...")])]),n("div",{staticClass:"answer"},[n("p",{staticClass:"title"},[t._v("問題文")]),n("p",{staticClass:"text"},[t._v(t._s(t.$route.params.translated))]),n("p",{staticClass:"title"},[t._v("原文")]),n("p",{staticClass:"text"},[t._v(t._s(t.$route.params.origin))])]),n("div",[n("button",{staticClass:"nextquestion",on:{click:function(e){return t.QuestionPage()}}},[t._v("次の問題へ")])])])},E=[],T={name:"AnswerPage",methods:{QuestionPage:function(){this.$router.push("/question")}}},Z=T,j=(0,l.Z)(Z,O,E,!1,null,"c9e33bfa",null),A=j.exports,q=function(){var t=this,e=t.$createElement;t._self._c;return t._m(0)},Q=[function(){var t=this,e=t.$createElement,n=t._self._c||e;return n("div",[n("h1",[t._v("このアプリについて")]),n("h2",[t._v("ドン・ブラコッコは有名なおとぎ話や小説をgoogle翻訳で再翻訳を繰り返し,その文章からもとの話の題名を当てるクイズです。")]),n("h1",[t._v("遊び方")]),n("h2",[t._v("①翻訳の回数を選択しよう!"),n("br"),t._v("翻訳の回数が多いほど話が支離滅裂になって難易度が上がるよ！")]),n("h2",[t._v("②スタートを押したら、多重翻訳された文章が出てくるよ！もとの文章を推測して物語の題名を答えてね！")])])}],L=n(1102),M=n.n(L),B=M(),F=(0,l.Z)(B,q,Q,!1,null,"384e3b9e",null),I=F.exports;a.Z.use(f.Z);var N=[{path:"/",name:"home",component:C},{path:"/question",name:"question",component:y},{path:"/answer",name:"AnswerPage",component:A},{path:"/explanation",name:"explanation",component:I}],z=new f.Z({mode:"history",base:"/",routes:N}),D=z;a.Z.config.productionTip=!1,new a.Z({router:D,render:function(t){return t(p)}}).$mount("#app")}},e={};function n(a){var r=e[a];if(void 0!==r)return r.exports;var o=e[a]={exports:{}};return t[a](o,o.exports,n),o.exports}n.m=t,function(){var t=[];n.O=function(e,a,r,o){if(!a){var s=1/0;for(u=0;u<t.length;u++){a=t[u][0],r=t[u][1],o=t[u][2];for(var i=!0,c=0;c<a.length;c++)(!1&o||s>=o)&&Object.keys(n.O).every((function(t){return n.O[t](a[c])}))?a.splice(c--,1):(i=!1,o<s&&(s=o));if(i){t.splice(u--,1);var l=r();void 0!==l&&(e=l)}}return e}o=o||0;for(var u=t.length;u>0&&t[u-1][2]>o;u--)t[u]=t[u-1];t[u]=[a,r,o]}}(),function(){n.n=function(t){var e=t&&t.__esModule?function(){return t["default"]}:function(){return t};return n.d(e,{a:e}),e}}(),function(){n.d=function(t,e){for(var a in e)n.o(e,a)&&!n.o(t,a)&&Object.defineProperty(t,a,{enumerable:!0,get:e[a]})}}(),function(){n.g=function(){if("object"===typeof globalThis)return globalThis;try{return this||new Function("return this")()}catch(t){if("object"===typeof window)return window}}()}(),function(){n.o=function(t,e){return Object.prototype.hasOwnProperty.call(t,e)}}(),function(){var t={143:0};n.O.j=function(e){return 0===t[e]};var e=function(e,a){var r,o,s=a[0],i=a[1],c=a[2],l=0;if(s.some((function(e){return 0!==t[e]}))){for(r in i)n.o(i,r)&&(n.m[r]=i[r]);if(c)var u=c(n)}for(e&&e(a);l<s.length;l++)o=s[l],n.o(t,o)&&t[o]&&t[o][0](),t[o]=0;return n.O(u)},a=self["webpackChunkfrontend"]=self["webpackChunkfrontend"]||[];a.forEach(e.bind(null,0)),a.push=e.bind(null,a.push.bind(a))}();var a=n.O(void 0,[998],(function(){return n(4845)}));a=n.O(a)})();
//# sourceMappingURL=app-legacy.828b50df.js.map