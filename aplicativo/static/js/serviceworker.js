var nm = 'electronica-pwa';

self.addEventListener('install', function(event) {
  event.waitUntil(
    caches.open(nm).then(function(cache) {
      return cache.addAll([
        '/encargado', '/venta', '/perfil', '/perfil/historial', '/ofertas', '/error'
      ]);
    })
  );
});

self.addEventListener('fetch', function(event) {
  var requestUrl = new URL(event.request.url);
    if (requestUrl.origin === location.origin) {
      if ((requestUrl.pathname === '/')) {
        event.respondWith(caches.match('/'));
        return;
      }
    }
    event.respondWith(
      caches.match(event.request).then(function(response) {
        return response || fetch(event.request);
      })
    );
});