from IPython.display import display, HTML

def loader(name="cal"):
    if name == "goog0l":
        return display(HTML('<style>.lds-ring {   display: inline-block;   position: relative;   width: 34px;   height: 34px; } .lds-ring div {   box-sizing: border-box;   display: block;   position: absolute;   width: 34px;   height: 34px;   margin: 4px;   border: 5px solid #cef;   border-radius: 50%;   animation: lds-ring 1.2s cubic-bezier(0.5, 0, 0.5, 1) infinite;   border-color: #cef transparent transparent transparent; } .lds-ring div:nth-child(1) {   animation-delay: -0.45s; } .lds-ring div:nth-child(2) {   animation-delay: -0.3s; } .lds-ring div:nth-child(3) {   animation-delay: -0.15s; } @keyframes lds-ring {   0% {     transform: rotate(0deg);   }   100% {     transform: rotate(360deg);   } }</style><div class="lds-ring"><div></div><div></div><div></div><div></div></div>'))
    elif name == "ylod":
        return display(HTML('''<style>.lds-hourglass {  display: inline-block;  position: relative;  width: 34px;  height: 34px;}.lds-hourglass:after {  content: " ";  display: block;  border-radius: 50%;  width: 34px;  height: 34px;  margin: 0px;  box-sizing: border-box;  border: 20px solid #dfc;  border-color: #dfc transparent #dfc transparent;  animation: lds-hourglass 1.2s infinite;}@keyframes lds-hourglass {  0% {    transform: rotate(0);    animation-timing-function: cubic-bezier(0.55, 0.055, 0.675, 0.19);  }  50% {    transform: rotate(900deg);    animation-timing-function: cubic-bezier(0.215, 0.61, 0.355, 1);  }  100% {    transform: rotate(1800deg);  }}</style><div class="lds-hourglass"></div>'''))
    elif name == "goog":
        return display(HTML(''' <style>.goog { border: 4px solid #DB4437; border-radius: 50%;  border-top: 4px solid #0F9D58; border-right: 4px solid #F4B400; border-bottom: 4px solid red; border-left: 4px solid #4285F4; width: 34px; height: 34px; -webkit-animation: spin 2s linear infinite; animation: spin 2s linear infinite; } @-webkit-keyframes spin { 0% { -webkit-transform: rotate(0deg); } 100% { -webkit-transform: rotate(360deg); }}@keyframes spin { 0% { transform: rotate(0deg); } 100% { transform: rotate(360deg); }}</style><div class="goog"></div>'''))
    elif name == "goog0":
        return display(HTML('''<style>
        .loader { border: 4px solid #f3f3f3; border-radius: 50%; border-top: 4px solid #3498db;  width: 32px; height: 32px; -webkit-animation: spin 2s linear infinite; animation: spin 2s linear infinite; } @-webkit-keyframes spin { 0% { -webkit-transform: rotate(0deg); } 100% { -webkit-transform: rotate(360deg); } } @keyframes spin { 0% { transform: rotate(0deg); }100% { transform: rotate(360deg); }}</style><div class="loader"></div>'''))
    else:
        print(f"Invalid loder Name: {name}")
      
def texter(TEXT, ty='2'):
    if ty == '1':
        return display(HTML('''<style>@import url(https://fonts.googleapis.com/css?family=Raleway:400,700,900,400italic,700italic,900italic);#wrapper {   font: 17px 'Raleway', sans-serif;animation: text-shadow 1.5s ease-in-out infinite;    margin-left: auto;    margin-right: auto;    }#container {    display: flex;    flex-direction: column;    float: left;     }@keyframes text-shadow { 0% 20% {          transform: translateY(-0.1em);        text-shadow:             0 0.1em 0 #0c2ffb,             0 0.1em 0 #2cfcfd,             0 -0.1em 0 #fb203b,             0 -0.1em 0 #fefc4b;    }    40% {          transform: translateY(0.1em);        text-shadow:             0 -0.1em 0 #0c2ffb,             0 -0.1em 0 #2cfcfd,             0 0.1em 0 #fb203b,             0 0.1em 0 #fefc4b;    }       60% {        transform: translateY(-0.1em);        text-shadow:             0 0.1em 0 #0c2ffb,             0 0.1em 0 #2cfcfd,             0 -0.1em 0 #fb203b,             0 -0.1em 0 #fefc4b;    }   }@media (prefers-reduced-motion: reduce) {    * {      animation: none !important;      transition: none !important;    }}</style><div id="wrapper"><div id="container">'''+TEXT+'''</div></div>'''))
    elif ty == '2':
        textcover = str(len(TEXT)*0.55)
        return display(HTML('''<style>@import url(https://fonts.googleapis.com/css?family=Anonymous+Pro);.line-1{font-family: 'Anonymous Pro', monospace;    position: relative;   border-right: 1px solid;    font-size: 15px;   white-space: nowrap;    overflow: hidden;    }.anim-typewriter{  animation: typewriter 0.4s steps(44) 0.2s 1 normal both,             blinkTextCursor 600ms steps(44) infinite normal;}@keyframes typewriter{  from{width: 0;}  to{width: '''+textcover+'''em;}}@keyframes blinkTextCursor{  from{border-right:2px;}  to{border-right-color: transparent;}}</style><div class="line-1 anim-typewriter">'''+TEXT+'''</div>'''))
    else:
        print(f"Invalid type: {ty}")
        
