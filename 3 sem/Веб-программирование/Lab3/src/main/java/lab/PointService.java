package lab;

import jakarta.ejb.Stateless;
import jakarta.persistence.EntityManager;
import jakarta.persistence.PersistenceContext;

@Stateless
public class PointService {
    @PersistenceContext(unitName = "pointManager")
    private EntityManager entityManager;

    public void addPoint(Point point) {
        entityManager.persist(point);
    }
}
