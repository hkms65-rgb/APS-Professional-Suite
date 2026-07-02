fetch('/api/modules').then(r=>r.json()).then(ms=>modules.innerHTML=ms.map(m=>`<div class='card'><h3>${m.name}</h3><p>${m.summary}</p></div>`).join(''))
