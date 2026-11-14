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
    brand: 'Volkswagen', model: 'up tsi', year: 2020,
  }), { headers: { 'Content-Type': 'application/json' }, timeout: '5s' });

  check(response, {
    'up tsi retorna 500 simulado pelo stub': (r) => r.status === 500,
    'up tsi retorna mensagem simulada': (r) =>
      r.status === 500 &&
      r.json('message') === "Internal server error: model 'up tsi' is not allowed.",
  });
  sleep(0.2);
}
