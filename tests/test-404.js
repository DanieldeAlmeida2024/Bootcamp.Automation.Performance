import http from 'k6/http';
import { check, sleep } from 'k6';

export const options = {
  vus: 2,
  iterations: 8,
  thresholds: { checks: ['rate>0.99'] },
};

export default function () {
  const url = (__ENV.BASE_URL || 'http://127.0.0.1:8080') + '/api/cars';
  const response = http.post(url, JSON.stringify({
    brand: 'Volkswagen', model: 'jetta', year: 2022,
  }), { headers: { 'Content-Type': 'application/json' }, timeout: '5s' });
  check(response, {
    'modelo não mapeado retorna 404': (r) => r.status === 404,
    'mensagem 404 é específica do mock': (r) =>
      r.status === 404 && r.json('message') === 'Vehicle not found.',
  });
  sleep(0.2);
}
