var cacheName = 'pwa-electronica'
var filesToCache = [
  '',
];
self.addEventListener('install',function(e){
  e.waitUntil(
      Promise.all([caches.open(STATIC_CACHE_NAME),caches.open(APP_CACHE_NAME),self.skipWaiting()]).then(function(storage){
          var static_cache = storage[0];
          var app_cache = storage[1];
          return Promise.all([static_cache.addAll(CACHE_STATIC),app_cache.addAll(CACHE_APP)]);
      })
  );
});

self.addEventListener('activate', function(e) {
  e.waitUntil(
      Promise.all([
          self.clients.claim(),
          caches.keys().then(function(cacheNames) {
              return Promise.all(
                  cacheNames.map(function(cacheName) {
                      if (cacheName !== APP_CACHE_NAME && cacheName !== STATIC_CACHE_NAME) {
                          console.log('deleting',cacheName);
                          return caches.delete(cacheName);
                      }
                  })
              );
          })
      ])
  );
});
self.addEventListener('fetch', function(event) {
  event.respondWith(
    caches.match(event.request).then(function(response) {
      return response || fetch(event.request);
    })
  );
});