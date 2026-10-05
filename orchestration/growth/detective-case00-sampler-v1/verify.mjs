const symbols=["BALL","STAR","BOLT","HEART","KEY","MOON"];
function permutations(items){if(items.length<=1)return [items];const out=[];for(let i=0;i<items.length;i++){const rest=items.slice(0,i).concat(items.slice(i+1));for(const tail of permutations(rest))out.push([items[i],...tail]);}return out;}
function valid(order){const p=Object.fromEntries(order.map((s,i)=>[s,i]));return p.BOLT===p.STAR+1&&p.BALL<p.STAR&&p.HEART>p.BOLT&&p.KEY<p.MOON&&p.HEART<p.MOON&&p.HEART!==4;}
const validOrders=permutations(symbols).filter(valid);
const expected="BALL -> STAR -> BOLT -> HEART -> KEY -> MOON";
const actual=validOrders.map(x=>x.join(" -> "));
if(validOrders.length!==1||actual[0]!==expected){throw new Error("CASE00 deterministic proof failed: "+JSON.stringify(actual));}
console.log(JSON.stringify({status:"PASS",permutations_checked:720,unique_solution:expected},null,2));
