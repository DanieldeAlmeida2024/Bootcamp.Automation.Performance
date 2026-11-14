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
    brand: 'Volkswagen', model: 'fusca', year: 1965,
  }), { headers: { 'Content-Type': 'application/json' }, timeout: '5s' });

  check(response, {
    'fusca retorna 201': (r) => r.status === 201,
    'fusca retorna mensagem do stub': (r) =>
      r.status === 201 && r.json('message') === 'Car successfully registered!',
    'fusca retorna ID fictício 6': (r) =>
      r.status === 201 && r.json('carId') === 6,
  });
  sleep(0.2);
}
