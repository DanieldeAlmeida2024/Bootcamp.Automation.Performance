import http from 'k6/http';
import { check, sleep } from 'k6';

export const options = {
  vus: 2,
  iterations: 8,
  thresholds: { checks: ['rate>0.99'] },
};

export default function () {
  const url = (__ENV.BASE_URL || 'http://127.0.0.1:8080') + '/api/cars';
  const response = http.get(url, { timeout: '5s' });
  check(response, {
    'GET retorna 200': (r) => r.status === 200,
    'GET retorna cinco veículos': (r) => r.status === 200 && r.json().length === 5,
    'primeiro veículo é Corolla': (r) =>
      r.status === 200 && r.json()[0].brand === 'Toyota' && r.json()[0].model === 'Corolla',
    'último veículo é BMW M3': (r) =>
      r.status === 200 && r.json()[4].brand === 'BMW' && r.json()[4].model === 'M3',
  });
  sleep(0.2);
}
