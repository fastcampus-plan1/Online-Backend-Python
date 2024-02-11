class DmAppRouter:
    app_label = "dm_app"
    database_name = "dm"

    def db_for_read(self, model, **hints):
        if model._meta.app_label == self.app_label:
            return self.database_name
        return None
    def db_for_write(self, model, **hints):
        if model._meta.app_label == self.app_label:
            return self.database_name
        return None
    def allow_relation(self, obj1, obj2, **hints):
        if obj1._meta.app_label == self.app_label or obj2._meta.app_label == self.app_label:
            return True
        return None
    def allow_migrate(self, db, app_label, model_name=None, **hints):
        return None